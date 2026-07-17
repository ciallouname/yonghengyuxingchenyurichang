


init -999 python:





    class VoiceSustainOn(Action):
        """
    开启语音持续
    """
        
        def __call__(self):
            preferences.voice_sustain = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return preferences.voice_sustain

    class VoiceSustainOff(Action):
        """
    关闭语音持续
    """
        
        def __call__(self):
            preferences.voice_sustain = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not preferences.voice_sustain

init -1400 python:

    class _CharacterVolumeValue(BarValue, DictEquality):
        
        def __init__(self, voice_tag):
            self.voice_tag = voice_tag
            self.step = None
            self.force_step = False
        
        def get_adjustment(self):
            if self.voice_tag not in persistent._character_volume:
                persistent._character_volume[self.voice_tag] = 1.0
            
            return ui.adjustment(
            range=1.0,
            value=persistent._character_volume[self.voice_tag],
            changed=self.set_volume,
            step=self.step,
            force_step=self.force_step)
        
        def set_volume(self, volume):
            persistent._character_volume[self.voice_tag] = volume
            renpy.restart_interaction()
        
        def get_style(self):
            return "slider", "vslider"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
