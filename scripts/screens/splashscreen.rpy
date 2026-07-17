

image caution_1 = "gui/custom2/caution_1.png"
image caution_2 = "gui/custom2/caution_2.png"


label splashscreen:
    if persistent.run_once == False:
        $ persistent.run_once = True
        $ SetDict(persistent._character_volume,"xingmi",0.6)()

    scene black

    show chunbai
    with dissolve


    show caution_1 with dissolve
    $ PlayRandomSystemVoice(8)()

    $ renpy.pause(0.5, hard=True)

    pause 1.5

    hide caution_1 with dissolve
    with Pause(0.5)


    show caution_2 with dissolve

    $ renpy.pause(0.5, hard=True)

    pause 3.5

    hide caution_2 with dissolve
    with Pause(0.5)
    $ PlayRandomSystemVoice(9)()


    if persistent.route_shiyu_done and persistent.route_xingmi_done and persistent.route_harem_ne_done and persistent.route_harem_ge_done:
        call achievement (23) from _call_achievement_25

    return


default quit_once = False

label quit:
    if persistent.system_voice_shiyu == False and persistent.system_voice_xingmi == False:
        return
    if quit_once:
        return
    $ quit_once = True

    window hide

    hide screen quick_menu

    $ PlayRandomSystemVoice(7)()
    if main_menu:
        show main_menu_bg:
            zoom 1.01
    else:
        show main_menu_bg:
            zoom 1.01
        with Dissolve(2.0)
    show title_logo_a:
        xpos 1205
        ypos 1025
    with Dissolve(2.0)
    if main_menu:
        pause (renpy.music.get_duration("voice")-2.0)
    else:
        pause (renpy.music.get_duration("voice")-4.0)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
