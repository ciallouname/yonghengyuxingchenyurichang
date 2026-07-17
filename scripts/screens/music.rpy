define asmr_track_files = ["audio/asmr/3.wav", "audio/asmr/4.wav", "audio/asmr/2.wav", "audio/asmr/1.wav","audio/asmr/5.wav"]
define asmr_track_names = ["音声 01", "音声 02", "音声 03", "音声 04", "主题曲"]
define asmr_track_titles = ["下播后的专属时间", "小小作家的休闲时刻", "盛夏·海滩·防晒霜", "清晨·突袭·过往趣事", "永恒星辰下的日常"]

define asmr_track_unlock_keys = ["route_shiyu_done", "route_xingmi_done", "route_harem_ne_done", "route_harem_ge_done", None]
define asmr_track_unlock_hints = ["通关时语线解锁", "通关星弥线解锁", "通关后宫线NE解锁", "通关后宫线GE解锁", ""]
default current_asmr_index = 0


init python:
    renpy.music.register_channel("asmr", mixer="asmr", loop=False)


init python:
    
    
    cached_duration = "00:00"
    cached_position = "00:00"
    cached_duration_raw = 0  
    
    def get_audio_duration(channel="asmr"):
        global cached_duration, cached_duration_raw
        duration = renpy.music.get_duration(channel)
        
        
        if duration and duration > 0:
            cached_duration_raw = int(duration)
            cached_duration = convert_format(cached_duration_raw)
            return cached_duration
        
        
        return cached_duration
    
    
    def get_audio_position(channel="asmr"):
        global cached_position, cached_duration_raw
        music_pos = renpy.music.get_pos(channel)
        
        
        if music_pos is not None and music_pos >= 0 and cached_duration_raw > 0:
            
            position = min(int(music_pos), cached_duration_raw)
            cached_position = convert_format(position)
            return cached_position
        
        
        return cached_position
    
    def convert_format(second):
        minute = second // 60
        second = second % 60
        result = ""
        
        
        if minute:
            
            if minute < 10:
                result = '0' + str(minute) + ":" + str(second)
                if second < 10:
                    result ='0' + str(minute) + ":" '0' + str(second)
            else:
                result = str(minute) + ":" + str(second)
                if second < 10:
                    result = str(minute) + '0' + str(second)
        
        else:
            
            if second < 10:
                result = '00:0' + str(second)
            else:
                result = '00:' + str(second)
        
        return result
    
    
    
    current_lyrics = []
    current_audio_file = ""
    
    
    cached_current_lyric = ""  
    cached_lyric_lines = []    
    
    
    lrc_debug_info = {"error": "", "path": "", "lines_read": 0, "lines_parsed": 0}
    
    def parse_lrc(lrc_path):
        """解析LRC歌词文件"""
        global lrc_debug_info
        lyrics = []
        lrc_debug_info["path"] = lrc_path
        lrc_debug_info["lines_read"] = 0
        lrc_debug_info["lines_parsed"] = 0
        lrc_debug_info["error"] = ""
        
        try:
            
            with renpy.open_file(lrc_path) as f:
                content = f.read()
                
                try:
                    text = content.decode('utf-8')
                except:
                    
                    try:
                        text = content.decode('utf-8-sig')  
                    except:
                        text = content.decode('gbk')  
                
                
                for line in text.split('\n'):
                    lrc_debug_info["lines_read"] += 1
                    line = line.strip()
                    if line.startswith('[') and ']' in line:
                        
                        time_tag = line[1:line.index(']')]
                        lyric_text = line[line.index(']')+1:].strip()
                        
                        
                        try:
                            if ':' in time_tag:
                                parts = time_tag.split(':')
                                minutes = int(parts[0])
                                seconds = float(parts[1])
                                time_in_seconds = minutes * 60 + seconds
                                lyrics.append((time_in_seconds, lyric_text))
                                lrc_debug_info["lines_parsed"] += 1
                        except Exception as e:
                            lrc_debug_info["error"] += f"解析行失败: {str(e)}; "
            
            lyrics.sort(key=lambda x: x[0])
        except Exception as e:
            lrc_debug_info["error"] = f"打开文件失败: {str(e)}"
        
        return lyrics
    
    def load_lyrics_for_audio(audio_path):
        """根据音频文件路径加载对应的LRC歌词文件"""
        global current_lyrics, current_audio_file
        
        
        if audio_path == current_audio_file and current_lyrics:
            return
        
        current_audio_file = audio_path
        
        
        lrc_path = audio_path.rsplit('.', 1)[0] + '.lrc'
        current_lyrics = parse_lrc(lrc_path)
    
    def get_current_lyric(channel="asmr"):
        """获取当前播放位置对应的歌词"""
        global current_lyrics, cached_current_lyric
        
        if not current_lyrics:
            return cached_current_lyric
        
        pos = renpy.music.get_pos(channel)
        if pos is None or pos < 0:
            return cached_current_lyric
        
        
        current_lyric = ""
        for i, (time, text) in enumerate(current_lyrics):
            if pos >= time:
                current_lyric = text
            else:
                break
        
        
        if current_lyric:
            cached_current_lyric = current_lyric
        
        return current_lyric if current_lyric else cached_current_lyric
    
    def get_lyric_lines(channel="asmr", context_lines=2):
        """获取当前歌词及前后几行，用于显示多行歌词

        始终返回固定行数 (context_lines * 2 + 1)，不足时用空字符串填充
        """
        global current_lyrics, cached_lyric_lines
        
        
        _empty = [("", False)] * (context_lines * 2 + 1)
        
        if not current_lyrics:
            return cached_lyric_lines if cached_lyric_lines else _empty
        
        pos = renpy.music.get_pos(channel)
        if pos is None or pos < 0:
            return cached_lyric_lines if cached_lyric_lines else _empty
        
        
        current_index = -1
        for i, (time, text) in enumerate(current_lyrics):
            if pos >= time:
                current_index = i
            else:
                break
        
        if current_index == -1:
            return cached_lyric_lines if cached_lyric_lines else _empty
        
        total_lines = context_lines * 2 + 1
        total_lyrics = len(current_lyrics)
        center_slot = context_lines  
        
        
        start_index = current_index - center_slot
        end_index = start_index + total_lines
        
        
        start_index = max(0, start_index)
        end_index = min(total_lyrics, end_index)
        
        
        result = []
        for i in range(start_index, end_index):
            is_current = (i == current_index)
            result.append((current_lyrics[i][1], is_current))
        
        
        current_pos = current_index - start_index
        pad_before = max(0, min(center_slot - current_pos, total_lines - len(result)))
        pad_after = max(0, total_lines - len(result) - pad_before)
        
        for _ in range(pad_before):
            result.insert(0, ("", False))
        for _ in range(pad_after):
            result.append(("", False))
        
        
        if result:
            cached_lyric_lines = result
        
        return result
    
    def is_asmr_track_unlocked(index):
        """检查指定索引的ASMR音轨是否已解锁"""
        key = asmr_track_unlock_keys[index]
        if key is None:
            return True  
        return getattr(persistent, key, False)
    
    def play_current_asmr():
        """播放当前选中的ASMR音轨并加载对应歌词"""
        if not is_asmr_track_unlocked(current_asmr_index):
            return
        track_file = asmr_track_files[current_asmr_index]
        renpy.music.play(track_file, channel="asmr", loop=False)
        load_lyrics_for_audio(track_file)
    
    def play_first_unlocked_asmr():
        """进入音乐界面时，找到第一个已解锁的ASMR音轨并播放"""
        global current_lyrics, current_audio_file, cached_current_lyric, cached_lyric_lines
        for i in range(len(asmr_track_files)):
            if is_asmr_track_unlocked(i):
                store.current_asmr_index = i
                
                current_audio_file = ""
                current_lyrics = []
                cached_current_lyric = ""
                cached_lyric_lines = []
                track_file = asmr_track_files[i]
                renpy.music.play(track_file, channel="asmr", loop=False)
                load_lyrics_for_audio(track_file)
                return
    
    def switch_asmr_track(index):
        """切换到指定ASMR音轨"""
        global current_lyrics, current_audio_file, cached_current_lyric, cached_lyric_lines
        if current_asmr_index == index:
            return
        if not is_asmr_track_unlocked(index):
            return
        store.current_asmr_index = index
        
        current_audio_file = ""
        current_lyrics = []
        cached_current_lyric = ""
        cached_lyric_lines = []
        
        track_file = asmr_track_files[index]
        renpy.music.play(track_file, channel="asmr", loop=False)
        load_lyrics_for_audio(track_file)

image extra_ad_bg:
    "gui/custom2/system/extra/extra_bg.png"
image extra_ad_title:
    "gui/custom2/system/extra/audio/extra_title_audio.png"
    xpos 61
    ypos 74
image extra_text_bg:
    "gui/custom2/system/extra/audio/extra_audio_data_bg.png"
    xpos 835
    ypos 238


screen music:
    tag menu

    key "hide_windows" action ShowMenu("main_menu_extral")

    add "extra_ad_bg"
    add "extra_ad_title"
    add "extra_text_bg"

    imagebutton:
        idle "gui/custom2/system/general_menu_back_normal.png"
        hover "gui/custom2/system/general_menu_back_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 2098
        ypos 1261
        action ShowMenu("main_menu_extral")

    imagebutton:
        idle "gui/custom2/system/extra/extra_menu_stand_normal.png"
        hover "gui/custom2/system/extra/extra_menu_stand_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1391
        ypos 67
        action [PlayRandomSystemVoice(4),ShowMenu("stand_mode")]

    imagebutton:
        idle "gui/custom2/system/extra/extra_menu_gallery_normal.png"
        hover "gui/custom2/system/extra/extra_menu_gallery_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1963
        ypos 67
        action [PlayRandomSystemVoice(2),ShowMenu("gallery")]


    timer 0.1:
        action [SetVariable('duration',get_audio_duration()),SetVariable('music_pos',get_audio_position())]
        repeat True

    vbox:
        xpos 141
        ypos 225
        spacing 20

        for i in range(len(asmr_track_files)):
            if is_asmr_track_unlocked(i):

                frame:
                    background None
                    xysize (575,179)
                    imagebutton:
                        idle "gui/custom2/system/extra/audio/extra_audio_list_bg_normal.png"
                        hover "gui/custom2/system/extra/audio/extra_audio_list_bg_click.png"
                        selected_idle "gui/custom2/system/extra/audio/extra_audio_list_bg_confim.png"
                        selected_hover "gui/custom2/system/extra/audio/extra_audio_list_bg_click.png"
                        selected (i == current_asmr_index)
                        activate_sound persistent.button_activate_sound
                        hover_sound persistent.button_hover_sound
                        action Function(switch_asmr_track, i)
                    text asmr_track_names[i]:
                        min_width 124
                        text_align 0
                        size 26
                        color "#ffffff"
                        font "ChillRoundGothic_Bold.ttf"
                        outlines [(3, "#7d959b", 0, 0)]
                        xpos 60
                        ypos 40
                    text asmr_track_titles[i]:
                        min_width 124
                        text_align 0
                        size 44
                        color "#ffffff"
                        font "ChillRoundGothic_Bold.ttf"
                        outlines [(3, "#7d959b", 0, 0)]
                        xpos 60
                        ypos 90
            else:

                frame:
                    background None
                    xysize (575,179)
                    imagebutton:
                        idle "gui/custom2/system/extra/audio/extra_audio_list_bg_normal.png"
                        hover "gui/custom2/system/extra/audio/extra_audio_list_bg_click.png"
                        sensitive False
                    text asmr_track_names[i]:
                        min_width 124
                        text_align 0
                        size 26
                        color "#ffffff7d"
                        font "ChillRoundGothic_Bold.ttf"
                        outlines [(3, "#7d959b7d", 0, 0)]
                        xpos 60
                        ypos 40
                    text asmr_track_unlock_hints[i]:
                        min_width 124
                        text_align 0
                        size 32
                        color "#ffffff7d"
                        font "ChillRoundGothic_Bold.ttf"
                        outlines [(3, "#7d959b7d", 0, 0)]
                        xpos 60
                        ypos 90




    imagebutton:
        xpos 846
        ypos 1038
        idle "gui/custom2/system/extra/audio/extra_audio_player_bo_pause_normal.png"
        hover "gui/custom2/system/extra/audio/extra_audio_player_bo_pause_click.png"
        selected_idle "gui/custom2/system/extra/audio/extra_audio_player_bo_play_normal.png"
        selected_hover "gui/custom2/system/extra/audio/extra_audio_player_bo_play_click.png"
        action PauseAudio(channel="asmr",value="toggle")
    imagebutton:
        xpos 1002
        ypos 1038
        idle "gui/custom2/system/extra/audio/extra_audio_player_bo_replay_normal.png"
        hover "gui/custom2/system/extra/audio/extra_audio_player_bo_replay_click.png"
        action Function(play_current_asmr)

    bar:
        value MyAudioPositionValue(channel='asmr', update_interval=0.01)
        xysize (817,54)
        xpos 1209
        ypos 1093

        left_bar "gui/custom2/system/extra/audio/extra_audio_player_tab_medium_bg_colored.png"
        right_bar "gui/custom2/system/extra/audio/extra_audio_player_tab_medium_bg.png"
        thumb "gui/custom2/system/extra/audio/extra_audio_player_tab_normal.png"
        hover_thumb "gui/custom2/system/extra/audio/extra_audio_player_tab_click.png"
        thumb_offset 29
        left_gutter 10
        right_gutter 10

    bar:
        value Preference("mixer asmr volume")
        xysize (284,54)
        xpos 2062
        ypos 1095

        left_bar "gui/custom2/system/extra/audio/extra_audio_player_tab_small_bg_colored.png"
        right_bar "gui/custom2/system/extra/audio/extra_audio_player_tab_small_bg.png"
        thumb "gui/custom2/system/extra/audio/extra_audio_player_tab_small_bo_normal.png"
        hover_thumb "gui/custom2/system/extra/audio/extra_audio_player_tab_small_bo_click.png"

        thumb_offset 25
        left_gutter 13
        right_gutter 13


    python:
        duration = get_audio_duration()
        music_pos = get_audio_position()
    text "时长":
        min_width 124
        text_align 0
        xpos 1220
        ypos 1150
        size 24
        color "#1f9092"
        font "ChillRoundGothic_Bold.ttf"
    text "[music_pos]/[duration]":
        min_width 124
        text_align 1.0
        xpos 1870
        ypos 1150
        size 24
        color "#1f9092"
        font "ChillRoundGothic_Bold.ttf"
    text "音量":
        min_width 124
        text_align 0
        xpos 2073
        ypos 1150
        size 24
        color "#1f9092"
        font "ChillRoundGothic_Bold.ttf"
    text "[int(preferences.get_mixer('asmr')*100)]%":
        min_width 124
        text_align 1.0
        xpos 2215
        ypos 1150
        size 24
        color "#1f9092"
        font "ChillRoundGothic_Bold.ttf"



    python:
        current_lyric_text = get_current_lyric()

        debug_pos = renpy.music.get_pos("asmr")
        debug_lyrics_count = len(current_lyrics)
        debug_current_file = current_audio_file

































































































    python:
        lyric_lines = get_lyric_lines(context_lines=4)
        if not lyric_lines:
            
            lyric_lines = [("", False)] * 9

        _lyric_spacing = 12
        _lyric_margin = 20  
        _lyric_slot_h = (775 - _lyric_margin * 2 - _lyric_spacing * (len(lyric_lines) - 1)) // len(lyric_lines)


    frame:
        background None
        xpos 835
        ypos 238
        xysize (1533, 775)

        has vbox
        xalign 0.5
        yalign 0.5
        spacing _lyric_spacing

        for lyric_text, is_current in lyric_lines:
            frame:
                background None
                xsize 1400
                xalign 0.5
                ysize _lyric_slot_h

                if lyric_text:
                    if is_current:

                        text "[lyric_text]":
                            size 54
                            color "#ffffff"
                            font "ChillRoundGothic_Bold.ttf"
                            xalign 0.5
                            yalign 0.5
                            text_align 0.5
                            xmaximum 1400
                    else:

                        text "[lyric_text]":
                            size 40
                            color "#ffffff7d"
                            font "ChillRoundGothic_Medium.ttf"
                            xalign 0.5
                            yalign 0.5
                            text_align 0.5
                            xmaximum 1400


    on "show" action [Stop("music"), Function(play_first_unlocked_asmr)]
    on "replace" action [Stop("music"), SetMute("asmr", False), Function(play_first_unlocked_asmr), SetVariable("persistent.music_entered", True)]


    on "replaced" action [Stop("asmr"), Play("music", config.main_menu_music)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
