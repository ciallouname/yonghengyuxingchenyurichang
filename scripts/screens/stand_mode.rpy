
image stand_bg:
    "gui/custom2/system/extra/stand/stand_bg.png"

image stand_data_bg:
    "gui/custom2/system/extra/stand/stand_data_bg.png"
    xpos 144
    ypos 599
image extra_title_stand:
    "gui/custom2/system/extra/stand/extra_title_stand.png"
    xpos 60
    ypos 74

default stand_zoom = 1.0
default stand_drag_x = 0
default stand_drag_y = 0
default hide_stand_ui = False

define data_group = [0,0,0,0,0,0]
define data_group_max = [2, 6, 2, 20, 1, len(bg_list)]




define stand_clothes_list = ["clothes1", "clothes2"]
define stand_pose_list_xingmi = ["front1", "front2", "front2_no", "front3", "front3_no", "side1"]
define stand_pose_list_shiyu = ["front2", "front1", "side1", "side2"]

define stand_face_list = [
    "smile", "wink", "oo", "shy", "bewilderment", "astonished", "pout", "not_good",
    "despise", "cachinnation", "smile_close", "laugh_open", "black", "sigh",
    "cat_mouth", "surprised_but", "focus", "calm", "eyes_closed", "cry"
]
define stand_manga_fx_list = [
    "hide_fx", "kp8wl", "kp1wl", "kp17wl", "kp2wl", "kp10wl", "kp10wl2",
    "kp13wl", "kp32wl", "kp18wl", "kp4wl", "kp28wl", "kp20wl", "kp29wl", "kp15wl"
]

init -999 python:

    def _reset_stand_state():
        """进入立绘模式时重置数据与视图状态。"""
        for i in range(len(data_group)):
            data_group[i] = 0
        store.stand_zoom = 0.7
        store.stand_drag_x = 400
        store.stand_drag_y = -150
        store.hide_stand_ui = False

    def _get_stand_group_max(index):
        """姿势(group_index=1)按角色动态max，漫符(group_index=4)共通。"""
        if index == 1:
            return len(stand_pose_list_xingmi) if data_group[0] == 0 else len(stand_pose_list_shiyu)
        if index == 4:
            return len(stand_manga_fx_list)
        return data_group_max[index]

    class StandDataInputLeft(Action):
        """
    左移数据
    """
        
        def __init__(self, group_index):
            self.group_index = group_index
        
        def __call__(self):
            max_val = _get_stand_group_max(self.group_index)
            data_group[self.group_index] -= 1
            if data_group[self.group_index] < 0:
                data_group[self.group_index] = max_val - 1
            
            if self.group_index == 0:
                pose_max = _get_stand_group_max(1)
                if data_group[1] >= pose_max:
                    data_group[1] = pose_max - 1
            renpy.restart_interaction()

    def _stand_dragged_callback(drags, drop):
        """立绘拖动结束后保存新位置（dragged 回调）"""
        if not drags:
            return
        d = drags[0]
        stand_ypos = int(180*stand_zoom) if data_group[0] == 0 else 0   
        store.stand_drag_x = d.x 
        store.stand_drag_y = d.y + stand_ypos
        renpy.restart_interaction()

    class StandDataInputRight(Action):
        """
    右移数据
    """
        def __init__(self, group_index):
            self.group_index = group_index
        
        def __call__(self):
            max_val = _get_stand_group_max(self.group_index)
            data_group[self.group_index] += 1
            if data_group[self.group_index] >= max_val:
                data_group[self.group_index] = 0
            
            if self.group_index == 0:
                pose_max = _get_stand_group_max(1)
                if data_group[1] >= pose_max:
                    data_group[1] = pose_max - 1
            renpy.restart_interaction()

    class StandZoomAtMouse(Action):
        """
    以鼠标位置为锚点缩放立绘，保证鼠标下的图像点屏幕位置不变。
    """
        def __init__(self, delta):
            self.delta = delta
        
        def __call__(self):
            old_zoom = store.stand_zoom
            new_zoom = max(0.2, min(3.0, old_zoom + self.delta))
            
            if abs(new_zoom - old_zoom) < 1e-9:
                return
            
            mouse_x, mouse_y = renpy.get_mouse_pos()
            
            old_x =   store.stand_drag_x
            old_y =   store.stand_drag_y
            
            
            local_x = (mouse_x - old_x) / old_zoom
            local_y = (mouse_y - old_y) / old_zoom
            new_x = mouse_x - local_x * new_zoom
            new_y = mouse_y - local_y * new_zoom
            
            store.stand_zoom = new_zoom
            store.stand_drag_x = int(new_x )
            store.stand_drag_y = int(new_y )
            
            renpy.restart_interaction()


screen stand_mode:
    tag menu

    key "hide_windows" action If(hide_stand_ui, SetVariable("hide_stand_ui", False), ShowMenu("main_menu_extral"))

    key "mousedown_4" action StandZoomAtMouse(0.1)
    key "mousedown_5" action StandZoomAtMouse(-0.1)

    add bg_list[data_group[5]]

    if not hide_stand_ui:
        add "stand_bg"

    python:
        role_name = "xingmi" if data_group[0] == 0 else "shiyu"
        pose_list = stand_pose_list_xingmi if data_group[0] == 0 else stand_pose_list_shiyu
        clothes = stand_clothes_list[min(data_group[2], len(stand_clothes_list) - 1)]
        pose = pose_list[min(data_group[1], len(pose_list) - 1)]
        clothes_posture = clothes + "_" + pose
        face = stand_face_list[min(data_group[3], len(stand_face_list) - 1)]
        manga_fx = stand_manga_fx_list[min(data_group[4], len(stand_manga_fx_list) - 1)]

        if face == "cry":
            skin = "skin_cry"
        elif face == "shy":
            skin = "skin_shy"
        elif face == "black":
            skin = "skin_black"
        else:
            skin = "skin_blush"
        stand_image_attrs = [role_name, skin, clothes_posture, face, manga_fx]
        stand_image_str = " ".join(stand_image_attrs)
        stand_ypos = int(180*stand_zoom) if data_group[0] == 0 else 0   
    fixed:
        xpos 0
        ypos 0
        xsize config.screen_width
        ysize config.screen_height
        drag:
            drag_name "stand"
            drag_offscreen True
            dragged _stand_dragged_callback
            xpos stand_drag_x
            ypos stand_drag_y - stand_ypos
            add Transform(stand_image_str, zoom=stand_zoom)

    if not hide_stand_ui:

        add "stand_data_bg"
        add "extra_title_stand"


        vbox:
            xpos 407
            ypos 726

            spacing 46

            for i in range(6):
                use stand_data_input(i)

        imagebutton:
            idle "gui/custom2/system/general_menu_back_normal.png"
            hover "gui/custom2/system/general_menu_back_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xpos 2098
            ypos 1261
            action ShowMenu("main_menu_extral")

        imagebutton:
            idle "gui/custom2/system/extra/extra_menu_audio_normal.png"
            hover "gui/custom2/system/extra/extra_menu_audio_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xpos 1327
            ypos 67
            action ShowMenu("music")

        imagebutton:
            idle "gui/custom2/system/extra/extra_menu_gallery_normal.png"
            hover "gui/custom2/system/extra/extra_menu_gallery_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xpos 1951
            ypos 67
            action [PlayRandomSystemVoice(2),ShowMenu("gallery")]

        imagebutton:
            idle "gui/custom2/system/extra/stand/stand_menu_hide_normal.png"
            hover "gui/custom2/system/extra/stand/stand_menu_hide_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            xpos 226
            ypos 1266
            action SetVariable("hide_stand_ui",True)

    on "show" action Function(_reset_stand_state)
    on "replace" action Function(_reset_stand_state)

screen stand_data_input(group_index):
    hbox:
        spacing 63

        imagebutton:
            idle "gui/custom2/system/extra/stand/stand_data_bo_left_normal.png"
            hover "gui/custom2/system/extra/stand/stand_data_bo_left_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            ypos 5
            action StandDataInputLeft(group_index)

        python:
            if group_index == 0:
                if data_group[0] == 0:
                    data_name = "星弥"
                else:
                    data_name = "时语"
            else:
                data_name = str(data_group[group_index]+1).zfill(3)
        text data_name:
            color "#ffffff"
            outlines [(3, "#116263", 0, 0)]
            font "ChillRoundGothic_Bold.ttf"
            min_width 75
            text_align 0
            size 36

        imagebutton:
            idle "gui/custom2/system/extra/stand/stand_data_bo_right_normal.png"
            hover "gui/custom2/system/extra/stand/stand_data_bo_right_click.png"
            activate_sound persistent.button_activate_sound
            hover_sound persistent.button_hover_sound
            ypos 5
            action StandDataInputRight(group_index)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
