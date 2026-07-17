





image titlenew_bg_2:
    "gui/custom2/title/title_bg.png"
    xalign 1.0

image titlenew_copyright:
    xpos 87
    ypos 1215
    "gui/custom2/title/title_copyright.png"

image title_logo_a:
    xpos 1205
    ypos 1025
    "gui/custom2/title/title_logo.png"

image chunbai:
    "images/chunbai.jpg"

image title_bg_3_a:
    xpos 927
    "gui/custom/title/title_bg_3_a.png"

image titlenew_bg_3_init:
    xpos 236
    "gui/custom/title/title_bg_2_char_sample.png"

image titlenew_copyright_init:
    xpos 33
    ypos 898
    "gui/custom/title/title_copyright.png"

image title_logo_a_init:
    xpos 1270
    ypos 57
    "gui/custom/title/title_logo_a.png"

image title_menu_gallery_sub_hints:
    xpos 465
    ypos 811
    "gui/custom/title/title_menu_gallery_sub_hints.png"

image title_divider:
    "gui/custom2/title/title_menu_main_sub.png"
    xalign 1.0



screen main_menu(force=False):
    tag menu




    add "chunbai"

    if force:
        add "main_menu_bg":
            zoom 1.01
        add "titlenew_bg_2"
        add "titlenew_copyright"
        add "title_logo_a"
    else:
        add "main_menu_bg" at main_menu_bg_transform:
            zoom 1.01
        add "titlenew_bg_2" at main_menu_bg_transform
        add "titlenew_copyright" at main_menu_bg_transform
        add "title_logo_a" at main_menu_bg_transform

    vbox:
        xpos 2452
        ypos 115
        spacing 40
        xanchor 1.0

        imagebutton:
            idle "gui/custom2/title/title_menu_main_start_normal.png"
            hover "gui/custom2/title/title_menu_main_start_click.png"
            at main_menu_show_btn(1.0 if not force else 0.0)
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xalign 1.0
            action [PlayRandomSystemVoice(10),Start()]

        imagebutton:
            idle "gui/custom2/title/title_menu_main_continue_normal.png"
            hover "gui/custom2/title/title_menu_main_continue_click.png"
            insensitive "gui/custom2/title/title_menu_main_continue_locked.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            at main_menu_show_btn(1.1 if not force else 0.1)
            xalign 1.0
            action SafeContinue()

        imagebutton:
            idle "gui/custom2/title/title_menu_main_load_normal.png"
            hover "gui/custom2/title/title_menu_main_load_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            at main_menu_show_btn(1.2 if not force else 0.2)
            xalign 1.0
            action [PlayRandomSystemVoice(5),ShowMenu("load")]

        add "title_divider" at main_menu_show_btn(1.3 if not force else 0.3)

        imagebutton:
            idle "gui/custom2/title/title_menu_main_system_normal.png"
            hover "gui/custom2/title/title_menu_main_system_click.png"
            hover_sound persistent.button_hover_sound
            at main_menu_show_btn(1.4 if not force else 0.4)
            xalign 1.0
            action [PlayRandomSystemVoice(1),ShowMenu("preferences")]

        if persistent.gallery_unlocked:
            imagebutton:
                idle "gui/custom2/title/title_menu_main_extra_normal.png"
                hover "gui/custom2/title/title_menu_main_extra_click.png"
                activate_sound persistent.button_activate_sound
                hover_sound persistent.button_hover_sound
                at main_menu_show_btn(1.5 if not force else 0.5)
                xalign 1.0
                action ShowMenu("main_menu_extral")
        else:
            add "gui/custom2/title/title_menu_main_extra_locked.png":
                at main_menu_show_btn(1.5 if not force else 0.5)
                xalign 1.0

        add "title_divider" at main_menu_show_btn(1.6 if not force else 0.6)

        imagebutton:
            idle "gui/custom2/title/title_menu_main_exit_normal.png"
            hover "gui/custom2/title/title_menu_main_exit_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            at main_menu_show_btn(1.7 if not force else 0.7)
            xalign 1.0
            action Quit(confirm=not main_menu)

image main_menu_extral_title:
    "gui/custom2/title/title_menu_extra_title.png"
    xpos 2007
    ypos 74
image main_menu_extral_line:
    "gui/custom2/title/title_menu_extra_sub.png"
    xpos 2466
    ypos 170

screen main_menu_extral():
    tag menu



    key "hide_windows" action ShowMenu("main_menu",force=True)

    add "main_menu_bg":
        zoom 1.01
    add "titlenew_bg_2"
    add "titlenew_copyright"
    add "title_logo_a"

    add "main_menu_extral_title" at main_menu_show_btn(0.0)
    add "main_menu_extral_line" at main_menu_show_btn(0.0)


    vbox:
        xpos 2452
        ypos 429
        spacing 40
        xanchor 1.0

        imagebutton:
            idle "gui/custom2/title/title_menu_extra_gallery_normal.png"
            hover "gui/custom2/title/title_menu_extra_gallery_click.png"
            at main_menu_show_btn(0.0)
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xalign 1.0
            action [PlayRandomSystemVoice(2),ShowMenu("gallery")]

        imagebutton:
            idle "gui/custom2/title/title_menu_extra_audio_normal.png"
            hover "gui/custom2/title/title_menu_extra_audio_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            at main_menu_show_btn(0.1)
            xalign 1.0
            action ShowMenu("music")

        imagebutton:
            idle "gui/custom2/title/title_menu_extra_stand_normal.png"
            hover "gui/custom2/title/title_menu_extra_stand_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            at main_menu_show_btn(0.2)
            xalign 1.0
            action [PlayRandomSystemVoice(4),ShowMenu("stand_mode")]

        add "title_divider" at main_menu_show_btn(0.3)

        imagebutton:
            idle "gui/custom2/title/title_menu_extra_back_normal.png"
            hover "gui/custom2/title/title_menu_extra_back_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            at main_menu_show_btn(0.4)
            xalign 1.0
            action ShowMenu("main_menu",force=True)


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
