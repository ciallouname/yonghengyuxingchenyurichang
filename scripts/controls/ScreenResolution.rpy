


init -999 python:
    
    
    
    
    
    
    
    def _screen_resolution_get_target_size(factor):
        """
        根据缩放因子计算目标窗口物理尺寸。

        不再使用 max_window_size 提前截断，因为 renpy.set_physical_size()
        内部已经有一致的可见区域约束，双重截断会导致窗口在某些屏幕上过小
        （例如 2K 屏幕上点击 1440p 只能得到 2379x1338）。
        """
        width = renpy.config.physical_width or renpy.config.screen_width
        height = renpy.config.physical_height or renpy.config.screen_height
        w = int(factor * width)
        h = int(factor * height)
        return (w, h)
    
    class ScreenResolution1440(Action):
        """
        设置屏幕分辨率1440
        """
        
        def __call__(self):
            persistent.screen_resolution = 1440
            persistent.fullscreen = False
            _preferences.maximized = False
            renpy.set_physical_size(_screen_resolution_get_target_size(1.0))
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.screen_resolution == 1440 and persistent.fullscreen == False
    
    class ScreenResolution1080(Action):
        """
        设置屏幕分辨率1080
        """
        
        def __call__(self):
            persistent.screen_resolution = 1080
            persistent.fullscreen = False
            _preferences.maximized = False
            renpy.set_physical_size(_screen_resolution_get_target_size(0.75))
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.screen_resolution == 1080 and persistent.fullscreen == False
    
    class ScreenResolution720(Action):
        """
        设置屏幕分辨率720
        """
        
        def __call__(self):
            persistent.screen_resolution = 720
            persistent.fullscreen = False
            _preferences.maximized = False
            renpy.set_physical_size(_screen_resolution_get_target_size(0.5))
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.screen_resolution == 720 and persistent.fullscreen == False
    
    class ScreenResolutionFullscreen(Action):
        """
        设置屏幕分辨率全屏
        """
        
        def __call__(self):
            persistent.fullscreen = True
            _preferences.fullscreen = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.fullscreen
    
    class ScreenResolutionWindowed(Action):
        """
        设置屏幕分辨率窗口化（同时恢复到当前分辨率对应的窗口尺寸）。
        """
        
        def __call__(self):
            persistent.fullscreen = False
            
            factor_map = {1440: 1.0, 1080: 0.75, 720: 0.5}
            factor = factor_map.get(persistent.screen_resolution, 0.5)
            renpy.set_physical_size(_screen_resolution_get_target_size(factor))
            renpy.restart_interaction()
        
        def get_selected(self):
            return not persistent.fullscreen

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
