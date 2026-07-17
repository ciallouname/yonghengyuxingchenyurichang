






screen choice(items):

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 0
        for i in items:
            frame:
                background None
                xysize (1287,165)
                imagebutton:
                    idle "gui/custom2/dialog/dialog_option_bg_normal.png"
                    hover "gui/custom2/dialog/dialog_option_bg_click.png"
                    activate_sound persistent.button_activate_sound
                    hover_sound persistent.button_hover_sound
                    action i.action
                text i.caption:
                    xalign 0.5
                    ypos 40
                    color "#ffffff"
                    outlines [(3, "#7d959b", 0, 0)]
                    size 46
                    font "SourceHanSansSC-Medium.otf"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
