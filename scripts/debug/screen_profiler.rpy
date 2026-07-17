


init python:
    import time


    _profile_enabled = False
    _profile_results = []

    def toggle_screen_profile():
        """切换性能分析状态"""
        global _profile_enabled
        _profile_enabled = not _profile_enabled
        
        if _profile_enabled:
            
            renpy.profile_screen("history",show=True,time=True,debug=True)
            renpy.notify("性能分析已开启 - 打开历史界面查看结果")
        else:
            renpy.notify("性能分析已关闭 - 查看控制台输出")

    def measure_history_screen():
        """测量历史界面的性能"""
        start_time = time.time()
        
        
        history_count = len(_history_list) if _history_list else 0
        
        
        elapsed = time.time() - start_time
        
        result = {
        "history_count": history_count,
        "measure_time": elapsed,
        "timestamp": time.strftime("%H:%M:%S")
    }
        
        _profile_results.append(result)
        return result


screen debug_profiler_keybind():
    key "shift_K_p" action Function(toggle_screen_profile)


init python:
    config.overlay_screens.append("debug_profiler_keybind")


screen debug_performance_info():
    zorder 100

    if _profile_enabled:
        frame:
            background "#000000AA"
            xalign 1.0
            yalign 0.0
            padding (10, 10)

            has vbox
            spacing 5
            text "性能分析已开启" size 20 color "#00FF00"
            text "历史记录数: [len(_history_list)]" size 16 color "#FFFFFF"
            text "按 Shift+P 关闭" size 14 color "#AAAAAA"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
