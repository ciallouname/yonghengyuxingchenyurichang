init -1500 python:
    
    class MyAudioPositionValue(BarValue, DictEquality):
        """
        :doc: value

        A value that shows the playback position of the audio file playing
        in `channel`.

        `update_interval`
            How often the value updates, in seconds.
        
        `adjustable`
            If True, the user can drag the bar to seek to a different position.
            Note: This will restart the audio from the selected position, which
            may cause a brief interruption. Default is False.
        """
        
        
        
        _duration_cache = {}
        _position_cache = {}  
        _seeking_flags = {}   
        
        def __init__(self, channel='music', update_interval=0.1, adjustable=True):
            self.channel = channel
            self.update_interval = update_interval
            self.adjustable = adjustable
            
            self.adjustment = None
            self.last_pos = 0.0
            self.initialized = False
            
            
            if self.channel not in MyAudioPositionValue._duration_cache:
                MyAudioPositionValue._duration_cache[self.channel] = 1.0
            if self.channel not in MyAudioPositionValue._position_cache:
                MyAudioPositionValue._position_cache[self.channel] = 0.0
            if self.channel not in MyAudioPositionValue._seeking_flags:
                MyAudioPositionValue._seeking_flags[self.channel] = False
        
        def get_pos_duration(self):
            pos = renpy.music.get_pos(self.channel) or 0.0
            duration = renpy.music.get_duration(self.channel)
            
            
            
            if duration and duration > 0:
                MyAudioPositionValue._duration_cache[self.channel] = duration
                MyAudioPositionValue._position_cache[self.channel] = pos
            else:
                duration = MyAudioPositionValue._duration_cache[self.channel]
                pos = MyAudioPositionValue._position_cache[self.channel]
            
            return pos, duration
        
        def changed(self, value):
            """
            Called when the user drags the bar to seek to a different position.

            Uses renpy.music.seek() (a lightweight runtime seek that reuses the
            existing decode pipeline) instead of renpy.music.play() with
            ``<from X>``.  This avoids re-opening, re-decrypting, and re-parsing
            the audio file on every drag event — making progress-bar scrubbing
            dramatically smoother for encrypted audio.
            """
            if not self.adjustable or MyAudioPositionValue._seeking_flags[self.channel]:
                return
            
            
            if not self.initialized:
                return
            
            
            current_pos = renpy.music.get_pos(self.channel) or 0.0
            if abs(value - current_pos) < 0.5:
                return
            
            
            playing = renpy.music.get_playing(self.channel)
            if not playing:
                return
            
            
            MyAudioPositionValue._seeking_flags[self.channel] = True
            MyAudioPositionValue._position_cache[self.channel] = value
            
            try:
                renpy.music.seek(value, channel=self.channel)
            finally:
                MyAudioPositionValue._seeking_flags[self.channel] = False
            
            renpy.restart_interaction()
        
        def get_adjustment(self):
            pos, duration = self.get_pos_duration()
            self.last_pos = pos
            
            if self.adjustable:
                self.adjustment = ui.adjustment(
                    value=pos, 
                    range=duration, 
                    adjustable=True,
                    changed=self.changed
                )
            else:
                self.adjustment = ui.adjustment(value=pos, range=duration, adjustable=False)
            
            self.initialized = True
            
            return self.adjustment
        
        def periodic(self, st):
            
            if MyAudioPositionValue._seeking_flags[self.channel]:
                return self.update_interval
            
            pos, duration = self.get_pos_duration()
            
            self.last_pos = pos
            self.adjustment.set_range(duration)
            self.adjustment.change(pos)
            
            return self.update_interval

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
