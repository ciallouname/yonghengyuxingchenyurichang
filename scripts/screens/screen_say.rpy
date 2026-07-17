









image dialog_charname_bg:
    "gui/custom2/dialog/dialog_charname_bg.png"

init -10 python:
    _MANGA_FX_ATTRS = {
    "kp8wl", "kp1wl", "kp17wl", "kp2wl", "kp10wl", "kp10wl2",
    "kp13wl", "kp32wl", "kp18wl", "kp4wl", "kp28wl", "kp20wl",
    "kp29wl", "kp15wl"
}


















    def _cache_side_image_state(event, interact=True, **kwargs):
        """
    在每个 say 语句开始时缓存当前的侧边图状态。
    缓存在普通 store 变量中，不受 _enter_menu() 的 context_dynamic 清空影响。
    """
        if event == "begin":
            tag = renpy.get_say_image_tag()
            store._last_side_tag = tag
            if tag is not None:
                attrs = renpy.get_attributes(tag, layer='master')
                store._last_side_attrs = attrs if attrs is not None else ()
            else:
                store._last_side_attrs = ()

    config.all_character_callbacks.append(_cache_side_image_state)

    def _get_side_no_manga(st, at):
        tag = renpy.get_say_image_tag()
        
        if tag is None:
            if renpy.store._side_image_attributes is None:
                
                
                tag = getattr(renpy.store, '_last_side_tag', None)
                attrs = getattr(renpy.store, '_last_side_attrs', ())
                if tag is None:
                    return Null(), None
            else:
                
                
                return Null(), None
        else:
            attrs = renpy.get_attributes(tag, layer='master')
            if attrs is None:
                attrs = ()
        
        filtered = tuple(a for a in attrs if a not in _MANGA_FX_ATTRS)
        prefix = config.side_image_prefix_tag or "side"
        name = " ".join((prefix, tag) + filtered)
        try:
            img = renpy.displayable(name)
        except Exception:
            img = Null()
        return img, None

image side_no_manga = DynamicDisplayable(_get_side_no_manga)



default _last_side_tag = None
default _last_side_attrs = ()




default _heroine_last_state = False
default _heroine_last_name = ""
default heroine = False
default heroine_name = ""


transform heroine_effect_fadeout:
    alpha 1.0
    pause 10.0
    linear 1.0 alpha 0.0


screen heroine_effect_screen():
    zorder 100
    add "gui/custom2/dialog/dialog_bg_heroine_sub_bg.png" at heroine_effect_fadeout:

        xpos -130
        ypos 68
    add "gui/custom2/dialog/dialog_bg_heroine_sub_icon.png" at heroine_effect_fadeout:

        xpos 6
        ypos 68

    text heroine_name at heroine_effect_fadeout:
        xpos 92
        ypos 68
        size 30
        color "#ffffff"
        outlines [(3, "#7d959b", 0, 0)]
        font "SourceHanSansSC-Bold.otf"



    timer 11.0 action Hide("heroine_effect_screen")

screen say(who, what):

    if persistent.instant_display_read_text and renpy.is_seen(ever = True):
        $ preferences.text_cps = 0
    else:

        if not _preferences.afm_enable:
            if persistent.normal_text_cps == 0:
                $ preferences.text_cps = 1
            elif persistent.normal_text_cps == 100:
                $ preferences.text_cps = 0
            else:
                $ preferences.text_cps = persistent.normal_text_cps

        else:
            if persistent.afm_text_cps == 0:
                $ preferences.text_cps = 1
            elif persistent.afm_text_cps == 100:
                $ preferences.text_cps = 0
            else:
                $ preferences.text_cps = persistent.afm_text_cps

    window:
        id "window"

        background Transform("gui/custom2/dialog/dialog_bg.png" if not heroine else "gui/custom2/dialog/dialog_bg_heroine.png", alpha=(100 - persistent.text_box_opacity)/100.0, xalign=0.5, yalign=1.0)

        if who is not None:

            hbox:
                id "namebox"
                style "namebox"

                spacing 15

                add "dialog_charname_bg"

                text who id "who":
                    size 46
                    yoffset -3
                    color "#ffffff"
                    outlines [(3, "#7d959b", 0, 0)]
                    font "SourceHanSansSC-Bold.otf"



                if _get_voice_info().filename is not None:
                    imagebutton:
                        yoffset 10
                        idle "gui/custom2/dialog/dialog_menu_revoice_normal.png"
                        hover "gui/custom2/dialog/dialog_menu_revoice_click.png"
                        selected_idle "gui/custom2/dialog/dialog_menu_revoice_selected.png"
                        selected_hover "gui/custom2/dialog/dialog_menu_revoice_selected.png"
                        if renpy.get_say_image_tag() == "xm":
                            action PlayCharacterVoice("xingmi",  _get_voice_info().filename,selected = True)
                        else:
                            action PlayCharacterVoice("shiyu",  _get_voice_info().filename,selected = True)


        text what id "what":
            size 40
            if persistent.text_outline:
                color "#ffffff"
            else:
                color "#7d959b"
            if persistent.text_outline:
                outlines [(3, "#7d959b", 0, 0)]
            line_spacing 5
            if persistent.text_bold:
                font "SourceHanSansSC-Bold.otf"
            else:
                font "SourceHanSansSC-Medium.otf"



    if isinstance(SideImage(), Null):
        add "gui/custom2/dialog/dialog_bg_sub.png":
            xpos 93
            ypos 1060
    else:
        frame:
            background None
            xysize (500,500)
            xpos 50
            ypos 940

            add "gui/custom2/dialog/dialog_char_img.png":
                xalign 0.5
                yalign 0.5
            add "gui/custom2/dialog/dialog_char_bg.png":
                xalign 0.5
                yalign 0.5
            if renpy.get_say_image_tag() == "xm":
                add AlphaMask(Crop((348,278,357,357),"side_no_manga"),"gui/custom2/dialog/dialog_char_radius.png"):
                    xalign 0.5
                    yalign 0.5
            elif renpy.get_say_image_tag() == "syq_":
                add AlphaMask(Crop((300,50,357,357),"side_no_manga"),"gui/custom2/dialog/dialog_char_radius.png"):
                    xalign 0.5
                    yalign 0.5
            else:
                add AlphaMask(Crop((348,198,357,357),"side_no_manga"),"gui/custom2/dialog/dialog_char_radius.png"):
                    xalign 0.5
                    yalign 0.5
            add "gui/custom2/dialog/dialog_char_hover.png":
                xalign 0.5
                yalign 0.5

    key "rollback" action ShowMenu("history")


    if heroine and (not _heroine_last_state or heroine_name != _heroine_last_name):
        timer 0.01 action [SetVariable("_heroine_last_state", True), SetVariable("_heroine_last_name", heroine_name), Show("heroine_effect_screen")]

    elif not heroine and _heroine_last_state:
        timer 0.01 action [SetVariable("_heroine_last_state", False), SetVariable("_heroine_last_name", ""), Hide("heroine_effect_screen")]

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height



style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

    line_overlap_split -10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
