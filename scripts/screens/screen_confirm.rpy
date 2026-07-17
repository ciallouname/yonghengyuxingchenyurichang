






image miniwindow_bg:
    "gui/custom2/small/miniwindow_bg.png"

image miniwindow_title_bg:
    xpos 279
    ypos 376
    "gui/custom2/small/miniwindow_title_bg.png"

screen confirm(message, yes_action, no_action):


    modal True

    zorder 200


    add "miniwindow_bg"
    add "miniwindow_title_bg"

    text _(message):
        color "#fff"
        size 48
        xpos 582
        ypos 455
        outlines [(3, "#7d959b", 0, 0)]
        xsize 1500


    imagebutton:
        xpos 1230
        ypos 563
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        idle "gui/custom2/small/miniwindow_bo_sure_normal.png"
        hover "gui/custom2/small/miniwindow_bo_sure_click.png"
        action yes_action

    imagebutton:
        xpos 1677
        ypos 563
        idle "gui/custom2/small/miniwindow_bo_cancel_normal.png"
        hover "gui/custom2/small/miniwindow_bo_cancel_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        action no_action


    key "hide_windows" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
