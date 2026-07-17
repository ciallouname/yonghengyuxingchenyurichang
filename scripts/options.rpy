












define config.name = _("永恒与星辰与日常")




define gui.show_name = True




define config.version = "1.45"





define gui.about = _p("""
""")





define build.name = "OurBriefEternity"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True












define config.main_menu_music = "audio/bgm/sundasora.ogg"









define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)






default preferences.text_cps = 0




default preferences.afm_time = 15














define config.save_directory = "OurBriefEternity-1749211016"






define config.window_icon = "gui/window_icon.png"






init python:

















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpym', None)
    build.classify('**.save', None)
    build.classify('**.pkf', None)
    build.classify('**.rar', None)
    build.classify('**.md', None)
    build.classify('game/.archive_key', None)
    build.classify('game/scripts/encryption_key.rpy', None)
    build.classify('game/scripts/encryption_key.rpyc', None)
    build.classify('game/helper', None)
    build.classify('game/audio/voice_source', None)
    build.classify('game/images/bg_source', None)
    build.classify('game/images/cg_source', None)


    build.archive('images', 'all')
    build.archive('scripts', 'all')
    build.archive('audio', 'all')
    build.archive('fonts', 'all')
    build.archive('video', 'all')


    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.webp', 'images')

    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/**.rpymc', 'scripts')

    build.classify('game/**.mp3', 'audio')
    build.classify('game/**.wav', 'audio')
    build.classify('game/**.ogg', 'audio')
    build.classify('game/**.lrc', 'audio')

    build.classify('game/**.ttf', 'fonts')
    build.classify('game/**.otf', 'fonts')

    build.classify('game/**.webm', 'video')




    build.documentation('*.html')
    build.documentation('*.txt')














define persistent.gallery_unlocked = False

define persistent.music_entered = False

default persistent.normal_text_cps = 30

default persistent.afm_text_cps = 30

default preferences.emphasize_audio = True

default persistent.text_box_opacity = 0


default preferences.fullscreen = True


define persistent.screen_resolution = 1440

define persistent.fullscreen = True

default preferences.skip_after_choices = True

default persistent.auto_after_choices = True

default persistent.instant_display_read_text = False

default persistent.text_bold = False

default persistent.text_outline = True


define config.default_music_volume = 0.35


define config.default_sfx_volume = 0.65


define config.default_voice_volume = 1



init python:
    renpy.music.register_channel("movie", mixer="movie", loop=True, stop_on_mute=False)

default preferences.voice_sustain = True


default persistent.stockings_color = 0



define config.steam_appid = 4169820

define persistent.button_hover_sound = "audio/sound/maou_se_system46.ogg"
define persistent.button_activate_sound = "audio/sound/maou_se_system47.ogg"


define config.side_image_same_transform = Dissolve(0.5)


define config.auto_voice = "audio/voice/{id}.ogg"


default preferences.voice_after_game_menu = True


define persistent.system_voice_shiyu = True
define persistent.system_voice_xingmi = True


define config.autosave_slots = 12


define persistent.run_once = False

define config.image_cache_size_mb = 1024





define persistent.op_watched = False


define persistent.ed_1_watched = False

define persistent.ed_2_watched = False

define persistent.ed_3_watched = False

define persistent.ed_4_watched = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
