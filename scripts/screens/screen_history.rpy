






init python:



    class MyAdjustment(renpy.display.behavior.Adjustment):
        
        def change(self, value, end_animation=True):
            
            if value > self._range and self._value == self._range:
                
                
                
                return Return()
            
            else:
                
                
                
                return renpy.display.behavior.Adjustment.change(self, value, end_animation)

init python:


    _history_prediction_started = False

    def start_history_prediction():
        """开始预加载历史界面"""
        global _history_prediction_started
        if not _history_prediction_started and _history_list:
            renpy.start_predict_screen("history")
            _history_prediction_started = True

    def stop_history_prediction():
        """停止预加载历史界面（可选，用于节省内存）"""
        global _history_prediction_started
        if _history_prediction_started:
            renpy.stop_predict_screen("history")
            _history_prediction_started = False


    def _history_predict_callback(event, interact=True, **kwargs):
        if event == "end" and interact:
            start_history_prediction()

    config.all_character_callbacks.append(_history_predict_callback)

    def add_side_image_to_history(h):
        """将当前显示的侧边图像添加到历史记录"""
        if renpy.store._side_image_attributes:
            filtered_attrs = tuple(a for a in renpy.store._side_image_attributes if a not in _MANGA_FX_ATTRS)
            h.side_image_attrs = filtered_attrs
            
            tag = renpy.get_say_image_tag()
            if tag:
                prefix = config.side_image_prefix_tag or "side"
                name = " ".join((prefix, tag) + filtered_attrs)
                try:
                    side_img = renpy.displayable(name)
                except Exception:
                    side_img = None
                h.side_image = side_img if side_img else None
            else:
                h.side_image = None
        else:
            h.side_image_attrs = None
            h.side_image = None

    config.history_callbacks.append(add_side_image_to_history)



image log_title:
    xpos 62
    ypos 75
    "gui/custom2/system/history/log_title.png"
image log_data_bg:
    xpos 100
    "gui/custom2/system/history/log_data_bg.png"


style history_who_text:
    size 46
    outlines [(2, "#fff", 0, 0)]
    xpos 280
    ypos 23
    min_width 234
    color "#1f9092"
    textalign 1.0
    font "SourceHanSansSC-Bold.otf"

style history_what_text:
    size 34
    outlines [(2, "#fff", 0, 0)]
    xpos 564
    ypos 15
    xsize 1500
    ysize 148
    line_spacing 15
    color "#1f9092"


style history_entry_frame:
    background None
    xsize 2084
    ysize 197



style history_jumpback_button is empty:
    xpos 390
    ypos 110

style history_jumpback_button_no_voice is empty:
    xpos 420
    ypos 110

style history_revoice_button is empty:
    xpos 465
    ypos 110



define _history_activate_sound = "audio/sound/maou_se_system47.ogg"
define _history_hover_sound = "audio/sound/maou_se_system46.ogg"






style history_vpgrid:
    xsize 2084
    ysize 897
    xpos 200
    ypos 247
    spacing 37


style history_vbar:
    xsize 62
    ysize 916
    xpos 2314
    ypos 231
    left_bar "gui/custom2/system/history/log_tab_bg.png"
    right_bar "gui/custom2/system/history/log_tab_bg.png"
    thumb "gui/custom2/system/history/log_tab_bo_normal.png"
    hover_thumb "gui/custom2/system/history/log_tab_bo_click.png"
    thumb_offset 16
    top_gutter 16
    bottom_gutter 16



style history_back_button is empty:
    xpos 2098
    ypos 1261

style history_title_button is empty:
    xpos 1741
    ypos 1261

screen history():
    modal True tag menu






    if main_menu:
        key "hide_windows" action Hide(transition=dissolve)
    else:
        key "hide_windows" action Return()

    add "general_bg"
    add "log_title"


    default adj = MyAdjustment(range=100, changed=None, adjustable=True)


    default history_vc = create_history_virtual_viewport(yadjustment=adj)

    python:
        history_vc.set_data_source(_history_list)

    viewport id "history_list":
        xsize 2084
        ysize 897
        xpos 200
        ypos 247
        yadjustment adj
        yinitial 1.0
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        add history_vc


    vbar:
        value YScrollValue("history_list")

        xysize (62,916)
        xpos 2314
        ypos 231

        left_bar "gui/custom2/system/history/log_tab_bg.png"
        right_bar "gui/custom2/system/history/log_tab_bg.png"
        thumb "gui/custom2/system/history/log_tab_bo_normal.png"
        hover_thumb "gui/custom2/system/history/log_tab_bo_click.png"

        thumb_offset 16
        top_gutter 16
        bottom_gutter 16

    imagebutton style "history_back_button":
        idle "gui/custom2/system/general_menu_back_normal.png"
        hover "gui/custom2/system/general_menu_back_click.png"
        activate_sound _history_activate_sound
        hover_sound _history_hover_sound
        action Return()

    if not main_menu:
        imagebutton style "history_title_button":
            idle "gui/custom2/system/general_menu_title_normal.png"
            hover "gui/custom2/system/general_menu_title_click.png"
            activate_sound _history_activate_sound
            hover_sound _history_hover_sound
            action MainMenu()




define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
