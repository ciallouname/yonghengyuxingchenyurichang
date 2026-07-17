




image extra_bg:
    "gui/custom2/system/extra/extra_bg.png"
image extra_title:
    xpos 60
    ypos 72
    "gui/custom2/system/extra/gallery/extra_title_gallery.png"
image extra_data_img_bg_nodata = "gui/custom/system/gallery/extra_data_img_bg_nodata.png"


init python:


    def seen_any(*names):
        """返回条件字符串：任意一张被 renpy.seen_image() 看到即解锁。"""
        return "(" + " or ".join("renpy.seen_image('{}')".format(n) for n in names) + ")"


    g = Gallery()

    g.locked_button = "gui/custom2/system/extra/gallery/extra_gallery_data_img_bg_nodata.png"
    g.hover_border="gui/custom2/system/extra/gallery/extra_gallery_data_fg_click.png"


    _cg100 = ["cg1","cg1001","cg1002","cg1003","cg1004","cg1005","cg1006","cg1007","cg1008","cg1009","cg10010","cg10012","cg10013","cg10015","cg10016","cg10018","cg10019","cg10021","cg10022","cg10023","cg10024","cg10027","cg10030","cg10031","cg10035","cg10040","cg10041","cg10042","cg10044","cg10045","cg10049","cg10052","cg10053","cg10054","cg10055","cg10056","cg10057","cg10058","cg10059"]
    _cond100 = seen_any(*_cg100)
    g.button("cg100")
    g.condition(_cond100)
    for _name in _cg100:
        g.image(_name)
        g.condition(_cond100)


    g.button("cg2")
    g.unlock_image("cg2")


    _cg30 = ["cg30","cg31","cg32","cg33","cg34","cg35","cg36"]
    _cond30 = seen_any(*_cg30)
    g.button("cg30")
    g.condition(_cond30)
    for _name in _cg30:
        g.image(_name)
        g.condition(_cond30)


    _cg400 = ["cg400","cg401","cg402","cg403","cg410","cg411","cg412","cg413","cg414","cg415","cg416","cg417","cg418","cg419","cg420","cg421","cg422","cg423","cg424","cg425","cg426","cg427"]
    _cond400 = seen_any(*_cg400)
    g.button("cg400")
    g.condition(_cond400)
    for _name in _cg400:
        g.image(_name)
        g.condition(_cond400)


    _cg5 = ["cg5","cg51","cg52","cg53","cg54","cg55","cg56"]
    _cond5 = seen_any(*_cg5)
    g.button("cg5")
    g.condition(_cond5)
    for _name in _cg5:
        g.image(_name)
        g.condition(_cond5)


    _cg6 = ["cg6","cg61","cg62","cg63","cg64","cg65"]
    _cond6 = seen_any(*_cg6)
    g.button("cg6")
    g.condition(_cond6)
    for _name in _cg6:
        g.image(_name)
        g.condition(_cond6)


    _cg7 = ["cg7","cg71","cg72","cg73","cg74","cg75"]
    _cond7 = seen_any(*_cg7)
    g.button("cg7")
    g.condition(_cond7)
    for _name in _cg7:
        g.image(_name)
        g.condition(_cond7)


    _cg8 = ["cg8","cg81"]
    _cond8 = seen_any(*_cg8)
    g.button("cg8")
    g.condition(_cond8)
    for _name in _cg8:
        g.image(_name)
        g.condition(_cond8)


    _cg15 = ["cg150","cg151","cg152","cg153","cg154","cg155","cg156","cg157","cg158","cg159","cg1510","cg1511","cg1512","cg1513","cg1514"]
    _cond15 = seen_any(*_cg15)
    g.button("cg15")
    g.condition(_cond15)
    for _name in _cg15:
        g.image(_name)
        g.condition(_cond15)


    _cg9 = ["cg9","cg91","cg92","cg93","cg94","cg95","cg96","cg97","cg98","cg99","cg910","cg911","cg912"]
    _cond9 = seen_any(*_cg9)
    g.button("cg9")
    g.condition(_cond9)
    for _name in _cg9:
        g.image(_name)
        g.condition(_cond9)


    _cg10 = ["cg10","cg101"]
    _cond10 = seen_any(*_cg10)
    g.button("cg10")
    g.condition(_cond10)
    for _name in _cg10:
        g.image(_name)
        g.condition(_cond10)


    _cg11 = ["cg11","cg111","cg112","cg113","cg114","cg115","cg116","cg117","cg118","cg119","cg1110","cg1111","cg1112","cg1113","cg1114"]
    _cond11 = seen_any(*_cg11)
    g.button("cg11")
    g.condition(_cond11)
    for _name in _cg11:
        g.image(_name)
        g.condition(_cond11)


    _cg12 = ["cg12","cg121","cg122","cg123","cg124","cg125","cg126","cg127","cg128","cg129","cg1210"]
    _cond12 = seen_any(*_cg12)
    g.button("cg12")
    g.condition(_cond12)
    for _name in _cg12:
        g.image(_name)
        g.condition(_cond12)


    _cg13 = ["cg13","cg131","cg132","cg133","cg134","cg135","cg136","cg137","cg138","cg1310","cg1311","cg1312","cg1313","cg1314","cg1315","cg1316","cg1317","cg1318"]
    _cond13 = seen_any(*_cg13)
    g.button("cg13")
    g.condition(_cond13)
    for _name in _cg13:
        g.image(_name)
        g.condition(_cond13)


    _cg14 = ["cg14","cg140","cg141","cg142","cg143","cg144","cg145","cg146","cg147"]
    _cond14 = seen_any(*_cg14)
    g.button("cg14")
    g.condition(_cond14)
    for _name in _cg14:
        g.image(_name)
        g.condition(_cond14)


    _cg16 = ["cg160","cg161","cg162","cg163"]
    _cond16 = seen_any(*_cg16)
    g.button("cg16")
    g.condition(_cond16)
    for _name in _cg16:
        g.image(_name)
        g.condition(_cond16)


    g.button("sd0")
    g.unlock_image("sd0")

    g.button("sd1")
    g.unlock_image("sd1")

    g.button("sd3")
    g.unlock_image("sd3")

    g.button("sd4")
    g.unlock_image("sd4")

    g.button("sd5")
    g.unlock_image("sd5")

    g.button("sd6")
    g.unlock_image("sd6")

    g.transition = dissolve
    g.image_screen = "gallery_image"


    gallery_thumbs = {
    "cg100":    Frame("images/cg/cg1.webp", xysize=(616,347)),
    "cg2":      Frame("images/cg/cg2.webp", xysize=(616,347)),
    "cg30":     Frame("images/cg/cg30.webp", xysize=(616,347)),
    "cg400":    Frame("images/cg/cg400.webp", xysize=(616,347)),
    "cg5":      Frame("images/cg/cg5.webp", xysize=(616,347)),
    "cg6":      Frame("images/cg/cg6.webp", xysize=(616,347)),
    "cg7":      Frame("images/cg/cg7.webp", xysize=(616,347)),
    "cg8":      Frame("images/cg/cg8.webp", xysize=(616,347)),
    "cg15":     Frame("images/cg/cg157.webp", xysize=(616,347)),
    "cg9":      Frame("images/cg/cg9.webp", xysize=(616,347)),
    "cg10":     Frame("images/cg/cg10.webp", xysize=(616,347)),
    "cg11":     Frame("images/cg/cg11.webp", xysize=(616,347)),
    "cg12":     Frame("images/cg/cg121.webp", xysize=(616,347)),
    "cg13":     Frame("images/cg/cg13.webp", xysize=(616,347)),
    "cg14":     Frame("images/cg/cg14.webp", xysize=(616,347)),
    "cg16":     Frame("images/cg/cg163.webp", xysize=(616,347)),
    "sd0":      Frame("images/cg/sd/sd0.webp", xysize=(616,347)),
    "sd1":      Frame("images/cg/sd/sd1.webp", xysize=(616,347)),
    "sd3":      Frame("images/cg/sd/sd3.webp", xysize=(616,347)),
    "sd4":      Frame("images/cg/sd/sd4.webp", xysize=(616,347)),
    "sd5":      Frame("images/cg/sd/sd5.webp", xysize=(616,347)),
    "sd6":      Frame("images/cg/sd/sd6.webp", xysize=(616,347)),
}


define gallery_groups = [
    "cg100", "cg400", "cg2", "cg30",   "cg6","cg5",
    "cg13","cg16", "cg7", "cg8", "cg15", "cg9", "cg10", "cg14", "cg11",
    "cg12",  "sd0", "sd1", "sd3", "sd4", "sd5", "sd6",
]


define groups_per_page = 6





define movie_items = [
    ("gui/custom2/system/extra/gallery/extra_gallery_moviethumbnail_OP.png",   "images/op.webm",   "op"),
    ("gui/custom2/system/extra/gallery/extra_gallery_moviethumbnail_PV.png",   "images/pv.webm",   "pv"),
    ("gui/custom2/system/extra/gallery/extra_gallery_moviethumbnail_ED01.png", "images/ed1.webm",  "ed1"),
    ("gui/custom2/system/extra/gallery/extra_gallery_moviethumbnail_ED02.png", "images/ed2.webm",  "ed2"),
    ("gui/custom2/system/extra/gallery/extra_gallery_moviethumbnail_ED03.png", "images/ed3.webm",  "ed3"),
    ("gui/custom2/system/extra/gallery/extra_gallery_moviethumbnail_ED04.png", "images/ed4.webm",  "ed4"),
]

init python:

    _mov_unlock_map = {
    "op":  "op_watched",
    "ed1": "ed_1_watched",
    "ed2": "ed_2_watched",
    "ed3": "ed_3_watched",
    "ed4": "ed_4_watched",
}

    def is_mov_unlocked(key):
        """检查视频是否已解锁。pv 始终解锁。"""
        if key == "pv":
            return True
        attr = _mov_unlock_map.get(key)
        if attr is None:
            return False
        return getattr(persistent, attr, False)

    def unlock_mov(key):
        """解锁指定视频（写入 persistent）。"""
        attr = _mov_unlock_map.get(key)
        if attr is not None:
            setattr(persistent, attr, True)

default gallery_page = 1
default gallery_mode = "cg"

init python:
    def play_movie(movie_path, unlock_key=None):
        """播放视频（全屏），支持右键停止，播放完毕自动回到画廊。
    若传入 unlock_key，播放后自动解锁该视频。"""
        old_dismiss = list(renpy.config.keymap.get("dismiss", []))
        if "mouseup_3" not in old_dismiss:
            renpy.config.keymap["dismiss"] = old_dismiss + ["mouseup_3"]
        try:
            renpy.call_in_new_context("play_movie_label", movie_path)
        finally:
            renpy.config.keymap["dismiss"] = old_dismiss
        if unlock_key is not None:
            unlock_mov(unlock_key)
        renpy.restart_interaction()


label play_movie_label(movie_path):
    $ renpy.movie_cutscene(movie_path)
    return


screen gallery:
    tag menu

    key "hide_windows" action ShowMenu("main_menu_extral")

    add "extra_bg"
    add "extra_title"

    imagebutton:
        idle "gui/custom2/system/general_menu_back_normal.png"
        hover "gui/custom2/system/general_menu_back_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 2098
        ypos 1261
        action ShowMenu("main_menu_extral")


    imagebutton:
        idle "gui/custom2/system/extra/extra_menu_stand_normal.png"
        hover "gui/custom2/system/extra/extra_menu_stand_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1243
        ypos 67
        action [PlayRandomSystemVoice(4),ShowMenu("stand_mode")]

    imagebutton:
        idle "gui/custom2/system/extra/extra_menu_audio_normal.png"
        hover "gui/custom2/system/extra/extra_menu_audio_click.png"
        activate_sound persistent.button_activate_sound
        hover_sound persistent.button_hover_sound
        xpos 1815
        ypos 67
        action ShowMenu("music")


    $ total_pages = max(1, (len(gallery_groups) + groups_per_page - 1) // groups_per_page)

    if gallery_mode == "cg":

        $ start_idx = (gallery_page - 1) * groups_per_page
        $ current_groups = gallery_groups[start_idx:start_idx + groups_per_page]


        grid 3 2:
            xsize 2305
            ysize 1098
            xpos 272
            ypos 311
            xspacing 92
            yspacing 93

            for group_name in current_groups:
                $ thumb = gallery_thumbs.get(group_name, None)
                if thumb is not None:
                    add g.make_button(group_name, thumb, xalign=0.5, yalign=0.5)


    hbox:
        xpos 246
        ypos 1267
        spacing 8

        for i in range(1, total_pages + 1):
            imagebutton:
                idle "gui/custom2/system/general_menu_page_{}_normal.png".format(i)
                hover "gui/custom2/system/general_menu_page_{}_click.png".format(i)
                selected_idle "gui/custom2/system/general_menu_page_{}_confim.png".format(i)
                selected_hover "gui/custom2/system/general_menu_page_{}_confim.png".format(i)
                selected (gallery_mode == "cg" and gallery_page == i)
                activate_sound persistent.button_activate_sound
                hover_sound persistent.button_hover_sound
                action [SetVariable("gallery_mode", "cg"), SetVariable("gallery_page", i)]


        add "gui/custom2/system/extra/gallery/extra_gallery_menu_page_sub_line.png":
            yoffset 20


        if gallery_mode == "mov":
            imagebutton:
                idle "gui/custom2/system/extra/gallery/extra_gallery_menu_page_mov_confim.png"
                hover "gui/custom2/system/extra/gallery/extra_gallery_menu_page_mov_confim.png"
                activate_sound persistent.button_activate_sound
                hover_sound persistent.button_hover_sound
                action NullAction()
        else:
            imagebutton:
                idle "gui/custom2/system/extra/gallery/extra_gallery_menu_page_mov_normal.png"
                hover "gui/custom2/system/extra/gallery/extra_gallery_menu_page_mov_click.png"
                activate_sound persistent.button_activate_sound
                hover_sound persistent.button_hover_sound
                action SetVariable("gallery_mode", "mov")

    if gallery_mode == "mov":

        grid 3 2:
            xsize 2305
            ysize 1098
            xpos 272
            ypos 311
            xspacing 92
            yspacing 93

            for _thumb, _movie, _key in movie_items:
                if is_mov_unlocked(_key):

                    imagebutton:
                        idle Fixed(
                            Frame(_thumb, xysize=(616, 347)),
                            Transform("gui/custom2/system/extra/gallery/extra_gallery_data_sub_mov.png", xalign=0.9, yalign=0.9),
                            xysize=(616, 347),
                        )
                        hover Fixed(
                            Frame(_thumb, xysize=(616, 347)),
                            Transform("gui/custom2/system/extra/gallery/extra_gallery_data_sub_mov.png", xalign=0.9, yalign=0.9),
                            "gui/custom2/system/extra/gallery/extra_gallery_data_fg_click.png",
                            xysize=(616, 347),
                        )
                        activate_sound persistent.button_activate_sound
                        hover_sound persistent.button_hover_sound
                        action Function(play_movie, _movie, _key)
                else:

                    add g.locked_button



screen gallery_image(locked, displayables, index, count, gallery, **properties):
    use _gallery(locked=locked, displayables=displayables, index=index, count=count, gallery=gallery, **properties)
    key "mousedown_3" action gallery.Return()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
