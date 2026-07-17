



init python:
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['hide_windows'].append('K_ESCAPE')
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['dismiss'].append('mouseup_5')
    config.keymap['help'].remove('K_F1')
    config.keymap['help'].remove('meta_shift_/')
    config.keymap['screenshot'].remove('alt_K_s')
    config.keymap['screenshot'].remove('alt_shift_K_s')
    config.keymap['screenshot'].remove('noshift_K_s')
    config.keymap['self_voicing'].remove('alt_K_v')
    config.keymap['self_voicing'].remove('K_v')
screen quick_menu():




    imagebutton:
        xpos 1351
        ypos 1354
        idle "gui/custom2/dialog/dialog_menu_auto_normal.png"
        hover "gui/custom2/dialog/dialog_menu_auto_click.png"
        selected_idle "gui/custom2/dialog/dialog_menu_auto_selected.png"
        selected_hover "gui/custom2/dialog/dialog_menu_auto_selected.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        action Preference("auto-forward", "toggle")

    imagebutton:
        xpos 1532
        ypos 1354
        idle "gui/custom2/dialog/dialog_menu_skip_normal.png"
        hover "gui/custom2/dialog/dialog_menu_skip_click.png"
        selected_idle "gui/custom2/dialog/dialog_menu_skip_selected.png"
        selected_hover "gui/custom2/dialog/dialog_menu_skip_selected.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        action Skip()
    imagebutton:
        xpos 1728
        ypos 1354
        idle "gui/custom2/dialog/dialog_menu_save_normal.png"
        hover "gui/custom2/dialog/dialog_menu_save_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        action [PlayRandomSystemVoice(12),ShowMenu("save")]
    imagebutton:
        xpos 1915
        ypos 1354
        idle "gui/custom2/dialog/dialog_menu_load_normal.png"
        hover "gui/custom2/dialog/dialog_menu_load_click.png"
        hover_sound persistent.button_hover_sound
        action [PlayRandomSystemVoice(5),ShowMenu("load")]
    imagebutton:
        xpos 2090
        ypos 1358
        idle "gui/custom2/dialog/dialog_menu_log_normal.png"
        hover "gui/custom2/dialog/dialog_menu_log_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        action ShowMenu("history")
    imagebutton:
        xpos 2314
        ypos 1357
        idle "gui/custom2/dialog/dialog_menu_sys_normal.png"
        hover "gui/custom2/dialog/dialog_menu_sys_click.png"
        hover_sound persistent.button_hover_sound
        action [PlayRandomSystemVoice(1),ShowMenu("preferences")]

    imagebutton:
        xpos 2449
        ypos 1073
        idle "gui/custom2/dialog/dialog_menu_hide_normal.png"
        hover "gui/custom2/dialog/dialog_menu_hide_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        action HideInterface()










style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
