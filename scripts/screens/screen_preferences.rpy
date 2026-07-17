






image general_bg:

    "gui/custom2/system/general_bg.png"
image sys_title:
    xpos 59
    ypos 73
    "gui/custom2/system/setting/sys_title.png"
image sys_data_basic_text:
    xpos 243
    ypos 196
    "gui/custom2/system/setting/sys_data_basic_text.png"

image sys_data_tab_bg_colored_disable:
    "gui/custom2/system/setting/sys_data_tab_bg_colored.png"
    alpha 0.5

define show_auto_text = False

screen preferences():
    modal True tag sys


    if main_menu:
        key "hide_windows" action [Hide(transition=dissolve),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]
    else:
        key "hide_windows" action [Return(),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]

    add "general_bg"
    add "sys_data_basic_text"
    add "sys_title"


    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo1_fullscreen_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo1_fullscreen_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo1_fullscreen_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo1_fullscreen_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 327
        ypos 271
        action ScreenResolutionFullscreen()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo1_windowed_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo1_windowed_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo1_windowed_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo1_windowed_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 789
        ypos 271
        action ScreenResolutionWindowed()


    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo2_1440p_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo2_1440p_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo2_1440p_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo2_1440p_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 327
        ypos 464
        action ScreenResolution1440()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo2_1080p_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo2_1080p_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo2_1080p_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo2_1080p_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 778
        ypos 464
        action ScreenResolution1080()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo2_720p_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo2_720p_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo2_720p_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo2_720p_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 327
        ypos 567
        action ScreenResolution720()


    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo3_allltext_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo3_alltext_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo3_allltext_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo3_allltext_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 516
        ypos 695
        action Preference("skip", "all")
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo3_readtext_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo3_readtext_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo3_readtext_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo3_readtext_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 857
        ypos 695
        action Preference("skip", "seen")
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo4_yes_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo4_yes_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo4_yes_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo4_yes_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 711
        ypos 828
        action InstantDisplayReadTextOn()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo4_no_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo4_no_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo4_no_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo4_no_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 959
        ypos 828
        action InstantDisplayReadTextOff()



    imagebutton:
        idle "gui/custom2/system/setting/3.png"
        hover "gui/custom2/system/setting/2.png"
        selected_idle "gui/custom2/system/setting/1.png"
        selected_hover "gui/custom2/system/setting/1.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 329
        ypos 1017
        action AutoAfterChoicesOn()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo5_stopauto_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo5_stopauto_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo5_stopauto_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo5_stopauto_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 778
        ypos 1016
        action AutoAfterChoicesOff()

    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo5_stillauto_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo5_stillauto_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo5_stillauto_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo5_stillauto_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 328
        ypos 1121
        action SkipAfterChoicesOn()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo5_stopskip_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo5_stopskip_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo5_stopskip_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo5_stopskip_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 778
        ypos 1119
        action SkipAfterChoicesOff()

    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo6_bold_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo6_bold_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo6_bold_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo6_bold_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1375
        ypos 271
        action TextBoldOn()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo6_unbold_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo6_unbold_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo6_unbold_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo6_unbold_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1838
        ypos 271
        action TextBoldOff()


    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo6_stroke_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo6_stroke_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo6_stroke_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo6_stroke_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1375
        ypos 375
        action TextOutlineOn()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_basic_bo6_unstroke_normal.png"
        hover "gui/custom2/system/setting/sys_data_basic_bo6_unstroke_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_basic_bo6_unstroke_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_basic_bo6_unstroke_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1838
        ypos 375
        action TextOutlineOff()

    imagebutton:
        idle "gui/custom2/system/general_menu_back_normal.png"
        hover "gui/custom2/system/general_menu_back_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 2098
        ypos 1261
        if main_menu:
            action [Hide(transition=dissolve),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]
        else:
            action [Return(),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]

    if not main_menu:
        imagebutton:
            idle "gui/custom2/system/general_menu_title_normal.png"
            hover "gui/custom2/system/general_menu_title_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xpos 1741
            ypos 1261
            action MainMenu()

    imagebutton:
        idle "gui/custom2/system/setting/sys_menu_reset_normal.png"
        hover "gui/custom2/system/setting/sys_menu_reset_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 145
        ypos 1261
        action [InstantDisplayReadTextOff(),SetVariable("persistent.text_box_opacity",0),TextOutlineOn(),TextBoldOff(),SkipAfterChoicesOn(),AutoAfterChoicesOn(),ScreenResolutionFullscreen(),Preference("skip", "seen"),SetVariable("persistent.normal_text_cps",30),SetVariable("persistent.afm_text_cps",30)]




    bar:
        value VariableValue("persistent.normal_text_cps",range=100)
        xysize (694,49)
        xpos 1458
        ypos 585

        left_bar "gui/custom2/system/setting/bar.png"
        right_bar "gui/custom2/system/setting/bar.png"
        thumb "gui/custom2/system/setting/bar_thum_1.png"
        hover_thumb "gui/custom2/system/setting/bar_thum.png"

        thumb_offset 13
        left_gutter 13
        right_gutter 13
    bar:
        value VariableValue("persistent.afm_text_cps",range=100)
        xysize (694,49)
        xpos 1458
        ypos 842

        left_bar "gui/custom2/system/setting/bar.png"
        right_bar "gui/custom2/system/setting/bar.png"
        thumb "gui/custom2/system/setting/bar_thum_1.png"
        hover_thumb "gui/custom2/system/setting/bar_thum.png"

        thumb_offset 13
        left_gutter 13
        right_gutter 13
    bar:
        value VariableValue("persistent.text_box_opacity",range=100)
        xysize (694,49)
        xpos 1458
        ypos 1102

        left_bar "gui/custom2/system/setting/bar.png"
        right_bar "gui/custom2/system/setting/bar.png"
        thumb "gui/custom2/system/setting/bar_thum_1.png"
        hover_thumb "gui/custom2/system/setting/bar_thum.png"

        thumb_offset 13
        left_gutter 13
        right_gutter 13


    add "gui/custom2/system/setting/text_box.png":
        xpos 1389
        ypos 644
    add "gui/custom2/system/setting/text_box.png":
        xpos 1389
        ypos 902

    add "gui/custom2/system/setting/text_box_bg.png":
        xpos 1389+143
        ypos 1157
        alpha (100 - persistent.text_box_opacity)/100.0
    add "gui/custom2/system/setting/text_box_cut.png":
        xpos 1389
        ypos 1157
    add "gui/custom2/system/setting/text_box_rect.png":
        xpos 1389
        ypos 1157
    text "此处背景为文本框透明度的演示":
        xpos 1546
        if persistent.text_outline:
            ypos 1163
        else:
            ypos 1165
        size 26
        if persistent.text_outline:
            color "#ffffff"
        else:
            color "#7d959b"
        if persistent.text_outline:
            outlines [(3, "#7d959b", 0, 0)]
        if persistent.text_bold:
            font "ChillRoundGothic_Bold.ttf"
        else:
            font "ChillRoundGothic_Medium.ttf"


    add "gui/custom2/system/setting/sys_menu_basic_confim.png":
        xpos 1695
        ypos 70


    imagebutton:
        idle "gui/custom2/system/setting/sys_menu_sound_normal.png"
        hover "gui/custom2/system/setting/sys_menu_sound_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 2053
        ypos 70
        action [ShowMenu("setting_sound") ,Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]

    default display_preview = True
    if display_preview:
        timer 0.2:
            action Show("setting")


screen setting():
    default display_preview = True
    if display_preview:
        timer 0.2:
            action [Show("setting_text_preview"), Show("setting_text_preview_auto")]


screen setting_text_preview():
    if persistent.normal_text_cps == 0:
        $ normal_text_cps = 1
    elif persistent.normal_text_cps == 100:
        $ normal_text_cps = 0
    else:
        $ normal_text_cps = persistent.normal_text_cps


    if normal_text_cps == 0:
        $ normal_time = 2
    else:
        $ normal_time = 15/normal_text_cps + 2

    text "此处为文本正常演出时的速度演示":
        xpos 1546
        if persistent.text_outline:
            ypos 651
        else:
            ypos 653
        size 26
        if persistent.text_outline:
            color "#ffffff"
        else:
            color "#7d959b"
        if persistent.text_outline:
            outlines [(3, "#7d959b", 0, 0)]
        if persistent.text_bold:
            font "ChillRoundGothic_Bold.ttf"
        else:
            font "ChillRoundGothic_Medium.ttf"
        slow_cps normal_text_cps

    timer normal_time repeat True action [Hide("setting_text_preview"), Show("setting_text_preview")]

screen setting_text_preview_auto():
    if persistent.afm_text_cps == 0:
        $ afm_text_cps = 1
    elif persistent.afm_text_cps == 100:
        $ afm_text_cps = 0
    else:
        $ afm_text_cps = persistent.afm_text_cps


    if afm_text_cps == 0:
        $ afm_time = 2
    else:
        $ afm_time = 15/afm_text_cps + 2

    text "此处为文本自动模式时的速度演示":
        xpos 1546
        if persistent.text_outline:
            ypos 908
        else:
            ypos 910
        size 26
        if persistent.text_outline:
            color "#ffffff"
        else:
            color "#7d959b"
        if persistent.text_outline:
            outlines [(3, "#7d959b", 0, 0)]
        if persistent.text_bold:
            font "ChillRoundGothic_Bold.ttf"
        else:
            font "ChillRoundGothic_Medium.ttf"
        slow_cps afm_text_cps

    timer afm_time repeat True action [Hide("setting_text_preview_auto"), Show("setting_text_preview_auto")]

image sys_data_sound_text:
    "gui/custom2/system/setting/sys_data_sound_text.png"
    xpos 243
    ypos 196

define voice_version = 1

screen setting_sound:
    modal True tag sys


    if main_menu:
        key "hide_windows" action [Hide(transition=dissolve),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]
    else:
        key "hide_windows" action [Return(),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]

    add "general_bg"
    add "sys_data_sound_text"
    add "sys_title"

    imagebutton:
        idle "gui/custom2/system/general_menu_back_normal.png"
        hover "gui/custom2/system/general_menu_back_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 2098
        ypos 1261
        if main_menu:
            action [Hide(transition=dissolve),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]
        else:
            action [Return(),Hide('setting'),Hide('setting_text_preview'),Hide('setting_text_preview_auto')]

    if not main_menu:
        imagebutton:
            idle "gui/custom2/system/general_menu_title_normal.png"
            hover "gui/custom2/system/general_menu_title_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xpos 1741
            ypos 1261
            action MainMenu()

    imagebutton:
        idle "gui/custom2/system/setting/sys_menu_reset_normal.png"
        hover "gui/custom2/system/setting/sys_menu_reset_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 145
        ypos 1261
        action [VoiceSustainOn(),Preference("main volume",1.0),Preference("music volume",0.05),SetMute("music",False),Preference("sound volume",0.2),SetMute("sfx",False),Preference("voice volume",1),SetMute("voice",False),Preference("mixer movie volume",1.0),SetVoiceMute("shiyu",False),SetVoiceMute("xingmi",False),SystemVoiceOnShiyu(),SystemVoiceOnXingmi(),SetDict(persistent._character_volume,"shiyu",1.0),SetDict(persistent._character_volume,"xingmi",0.6)]



    add "gui/custom2/system/setting/sys_menu_sound_confim.png":
        xpos 2053
        ypos 70

    imagebutton:
        idle "gui/custom2/system/setting/sys_menu_basic_normal.png"
        hover "gui/custom2/system/setting/sys_menu_basic_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1695
        ypos 70
        action ShowMenu("preferences")



    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_yes_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_yes_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_yes_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_yes_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1373
        ypos 428
        action VoiceSustainOff()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_no_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_no_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_no_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_no_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1824
        ypos 428
        action VoiceSustainOn()


    bar:
        value Preference("main volume")
        xysize (694,49)
        xpos 403
        ypos 279

        left_bar "gui/custom2/system/setting/bar.png"
        right_bar "gui/custom2/system/setting/bar.png"
        thumb "gui/custom2/system/setting/bar_thum_1.png"
        hover_thumb "gui/custom2/system/setting/bar_thum.png"

        thumb_offset 13
        left_gutter 13
        right_gutter 13













    if not preferences.get_mute("music"):
        bar:
            value Preference("music volume")
            xysize (694,49)
            xpos 403
            ypos 428

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"

            thumb_offset 13
            left_gutter 13
            right_gutter 13
    else:
        $ music_volume = preferences.get_mixer("music")
        bar:
            value music_volume
            xysize (694,49)
            xpos 403
            ypos 428
            range 1.0

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13



    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_mute_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_mute_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1031
        ypos 358
        action ToggleMute("music")




    if not preferences.get_mute("sfx"):
        bar:
            value Preference("sound volume")
            xysize (694,49)
            xpos 403
            ypos 574

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13
    else:
        $ sound_volume = preferences.get_mixer("sfx")
        bar:
            value sound_volume
            xysize (694,49)
            xpos 403
            ypos 574
            range 1.0

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13



    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_mute_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_mute_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1031
        ypos 505
        action ToggleMute("sfx")


    if not preferences.get_mute("voice"):
        bar:
            value Preference("voice volume")
            xysize (694,49)
            xpos 1453
            ypos 282

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13
    else:
        $ voice_volume = preferences.get_mixer("voice")
        bar:
            value voice_volume
            xysize (694,49)
            xpos 1453
            ypos 282
            range 1.0

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13



    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_mute_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_mute_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 2078
        ypos 214
        action ToggleMute("voice")

    add "gui/custom2/system/setting/mute.png":
        xpos 1015
        ypos 868

    add "gui/custom2/system/setting/mute.png":
        xpos 2030
        ypos 868


    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_mute_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_mute_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 954
        ypos 865
        action CharaterVoiceAllMuteShiyu()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_mute_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_mute_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_mute_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1975
        ypos 865
        action CharaterVoiceAllMuteXingmi()


    if voice_version == 0:
        imagebutton:
            idle "gui/custom2/system/setting/sys_data_sound_char_test_normal.png"
            hover "gui/custom2/system/setting/sys_data_sound_char_test_click.png"
            selected_idle "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            selected_hover "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            xpos 760
            ypos 930
            action PlayCharacterVoice("shiyu", "audio/system/C11-1.ogg",selected=True)
    else:
        imagebutton:
            idle "gui/custom2/system/setting/sys_data_sound_char_test_normal.png"
            hover "gui/custom2/system/setting/sys_data_sound_char_test_click.png"
            selected_idle "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            selected_hover "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            xpos 760
            ypos 930
            action PlayCharacterVoice("shiyu", "audio/system/C12-1.ogg",selected=True)

    on "replace":
        action SetVariable("voice_version", renpy.random.choice([0,1]))

    if voice_version == 0:
        imagebutton:
            idle "gui/custom2/system/setting/sys_data_sound_char_test_normal.png"
            hover "gui/custom2/system/setting/sys_data_sound_char_test_click.png"
            selected_idle "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            selected_hover "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            xpos 1775
            ypos 930
            action PlayCharacterVoice("xingmi", "audio/system/D11-1.ogg",selected=True)
    else:
        imagebutton:
            idle "gui/custom2/system/setting/sys_data_sound_char_test_normal.png"
            hover "gui/custom2/system/setting/sys_data_sound_char_test_click.png"
            selected_idle "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            selected_hover "gui/custom2/system/setting/sys_data_sound_char_test_confim.png"
            xpos 1775
            ypos 930
            action PlayCharacterVoice("xingmi", "audio/system/D12-1.ogg",selected=True)


    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_have_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_have_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 756
        ypos 1006
        action SetVoiceMute("shiyu",False)
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_not_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_not_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 963
        ypos 1006
        action SetVoiceMute("shiyu",True)
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_have_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_have_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 756
        ypos 1077
        action SystemVoiceOnShiyu()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_not_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_not_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 963
        ypos 1077
        action SystemVoiceOffShiyu()

    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_have_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_have_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1771
        ypos 1006
        action SetVoiceMute("xingmi",False)
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_not_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_not_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1979
        ypos 1006
        action SetVoiceMute("xingmi",True)
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_have_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_have_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_have_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1771
        ypos 1077
        action SystemVoiceOnXingmi()
    imagebutton:
        idle "gui/custom2/system/setting/sys_data_sound_char_not_normal.png"
        hover "gui/custom2/system/setting/sys_data_sound_char_not_click.png"
        selected_idle "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        selected_hover "gui/custom2/system/setting/sys_data_sound_char_not_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1979
        ypos 1077
        action SystemVoiceOffXingmi()


    if "shiyu" not in persistent._voice_mute:
        bar:
            value SetCharacterVolume("shiyu")
            xysize (694,49)
            xpos 400
            ypos 1163
            range 1.0

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13
    else:
        bar:
            value GetCharacterVolume("shiyu")
            xysize (694,49)
            xpos 400
            ypos 1163
            range 1.0

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13

    if "xingmi" not in persistent._voice_mute:
        bar:
            value SetCharacterVolume("xingmi")
            xysize (694,49)
            xpos 1420
            ypos 1163
            range 1.0

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13
    else:
        $ voice_volume = GetCharacterVolume("xingmi")
        bar:
            value voice_volume
            xysize (694,49)
            xpos 1420
            ypos 1163
            range 1.0

            left_bar "gui/custom2/system/setting/bar.png"
            right_bar "gui/custom2/system/setting/bar.png"
            thumb "gui/custom2/system/setting/bar_thum_1.png"
            hover_thumb "gui/custom2/system/setting/bar_thum.png"


            thumb_offset 13
            left_gutter 13
            right_gutter 13

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
