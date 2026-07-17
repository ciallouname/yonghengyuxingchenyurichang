







screen save():
    modal True

    use file_slots(_("保存"))


screen load():
    modal True

    use file_slots(_("读取游戏"))


image sl_title_load:
    xpos 59
    ypos 74
    "gui/custom2/system/SL/sl_title_load.png"

image sl_title_save:
    xpos 59
    ypos 74
    "gui/custom2/system/SL/sl_title_save.png"

image sl_data_img_bg_nodata:
    "gui/custom2/system/SL/sl_data_img_bg_nodata.png"

image sl_data_date_bg:
    ypos 267
    "gui/custom2/system/SL/sl_data_date_bg.png"

image sl_data_subline:
    xpos 106
    ypos 550
    "gui/custom2/system/SL/sl_data_subline.png"


screen file_slots(title):
    modal True

    if main_menu:
        key "hide_windows" action Hide(transition=dissolve)
    else:
        key "hide_windows" action Return()

    add "general_bg"

    if title == "保存":
        add "sl_title_save"
    else:
        add "sl_title_load"

    imagebutton:
        idle "gui/custom2/system/general_menu_back_normal.png"
        hover "gui/custom2/system/general_menu_back_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 2098
        ypos 1261
        if main_menu:
            action Hide(transition=dissolve)
        else:
            action Return()

    if not main_menu:
        imagebutton:
            idle "gui/custom2/system/general_menu_title_normal.png"
            hover "gui/custom2/system/general_menu_title_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xpos 1741
            ypos 1261
            action MainMenu()
    grid 4 3:
        xpos 208
        ypos 202

        xspacing 87
        yspacing 34

        for i in range(12):

            $ slot = i + 1

            frame:
                background None
                xysize (462,306)

                add "gui/custom2/system/SL/sl_data_img_bg_nodata.png"

                add "sl_data_date_bg"

                add FileScreenshot(slot)

                imagebutton:
                    idle "gui/custom2/system/SL/sl_data_img_bg_empty.png"
                    hover "gui/custom2/system/SL/sl_data_img_fg_click.png"
                    activate_sound persistent.button_activate_sound
                    hover_sound persistent.button_hover_sound
                    action SafeFileAction(slot)

                text FileTime(slot, format=_("{#file_time}%Y/%m/%d %H:%M:%S"), empty=_("")):
                    color "#1f9092"
                    size 24
                    xpos 145
                    ypos 273
                    font "ChillRoundGothic_Bold.ttf"

                if FileNewest(slot):
                    add "gui/custom2/system/SL/sl_data_new.png":
                        xpos -32
                        ypos 18

    imagebutton:
        xpos 149
        ypos 1267
        idle "gui/custom2/system/SL/sl_menu_page_auto_normal.png"
        hover "gui/custom2/system/SL/sl_menu_page_auto_click.png"
        selected_idle "gui/custom2/system/SL/sl_menu_page_auto_confim.png"
        selected_hover "gui/custom2/system/SL/sl_menu_page_auto_confim.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        action FilePage("auto")
    $ page_num = 0
    hbox:
        xpos 246
        ypos 1267
        spacing 8

        imagebutton:
            idle "gui/custom2/system/general_menu_page_1_normal.png"
            hover "gui/custom2/system/general_menu_page_1_click.png"
            selected_idle "gui/custom2/system/general_menu_page_1_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_1_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(1)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_2_normal.png"
            hover "gui/custom2/system/general_menu_page_2_click.png"
            selected_idle "gui/custom2/system/general_menu_page_2_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_2_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(2)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_3_normal.png"
            hover "gui/custom2/system/general_menu_page_3_click.png"
            selected_idle "gui/custom2/system/general_menu_page_3_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_3_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(3)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_4_normal.png"
            hover "gui/custom2/system/general_menu_page_4_click.png"
            selected_idle "gui/custom2/system/general_menu_page_4_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_4_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(4)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_5_normal.png"
            hover "gui/custom2/system/general_menu_page_5_click.png"
            selected_idle "gui/custom2/system/general_menu_page_5_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_5_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(5)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_6_normal.png"
            hover "gui/custom2/system/general_menu_page_6_click.png"
            selected_idle "gui/custom2/system/general_menu_page_6_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_6_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(6)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_7_normal.png"
            hover "gui/custom2/system/general_menu_page_7_click.png"
            selected_idle "gui/custom2/system/general_menu_page_7_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_7_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(7)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_8_normal.png"
            hover "gui/custom2/system/general_menu_page_8_click.png"
            selected_idle "gui/custom2/system/general_menu_page_8_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_8_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(8)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_9_normal.png"
            hover "gui/custom2/system/general_menu_page_9_click.png"
            selected_idle "gui/custom2/system/general_menu_page_9_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_9_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(9)
        imagebutton:
            idle "gui/custom2/system/general_menu_page_10_normal.png"
            hover "gui/custom2/system/general_menu_page_10_click.png"
            selected_idle "gui/custom2/system/general_menu_page_10_confim.png"
            selected_hover "gui/custom2/system/general_menu_page_10_confim.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            action FilePage(10)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
