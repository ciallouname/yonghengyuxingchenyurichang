init -999 python:
    import sys, os

    def get_dpi():
        """
    获取当前系统的 DPI 值，包含跨平台检测。
    返回 (dpi, dpi_scale, actual_w, actual_h)
      - dpi: 屏幕 DPI 值（标准 96）
      - dpi_scale: 缩放倍率（dpi / 96）
      - actual_w/h: 窗口实际占用的物理像素尺寸
    """
        phys_w, phys_h = renpy.get_physical_size()
        dpi = 96
        if sys.platform == "win32":
            try:
                import ctypes
                dc = ctypes.windll.user32.GetDC(0)
                dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, 88)  
                ctypes.windll.user32.ReleaseDC(0, dc)
            except:
                pass
        elif sys.platform == "darwin":
            try:
                import ctypes
                ctypes.cdll.LoadLibrary("/System/Library/Frameworks/AppKit.framework/AppKit")
                objc = ctypes.cdll.LoadLibrary("/usr/lib/libobjc.dylib")
                objc.objc_getClass.restype = ctypes.c_void_p
                objc.sel_registerName.restype = ctypes.c_void_p
                objc.objc_msgSend.restype = ctypes.c_void_p
                objc.objc_msgSend.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
                cls = objc.objc_getClass(b"NSScreen")
                sel_main = objc.sel_registerName(b"mainScreen")
                sel_scale = objc.sel_registerName(b"backingScaleFactor")
                screen = objc.objc_msgSend(cls, sel_main)
                objc.objc_msgSend.restype = ctypes.c_double
                scale = objc.objc_msgSend(screen, sel_scale)
                dpi = int(96 * scale)
            except:
                pass
        elif sys.platform.startswith("linux"):
            try:
                import subprocess, re
                out = subprocess.check_output(["xrdb", "-query"], text=True)
                m = re.search(r"Xft\.dpi:\s*(\d+)", out)
                if m:
                    dpi = int(m.group(1))
            except:
                pass
        elif hasattr(renpy, "android") or "ANDROID_ARGUMENT" in os.environ:
            try:
                from jnius import autoclass
                metrics = autoclass("org.renpy.android.PythonActivity").mActivity \
                .getResources().getDisplayMetrics()
                dpi = int(metrics.densityDpi)
            except:
                pass
        dpi_scale = dpi / 96.0
        actual_w = int(phys_w * dpi_scale)
        actual_h = int(phys_h * dpi_scale)
        return dpi, dpi_scale, actual_w, actual_h

    def select_menu_bg(st, at):
        dpi, dpi_scale, actual_w, actual_h = get_dpi()
        if actual_h <= 720:
            name = "main_menu_bg_720p"
        elif actual_h <= 1080:
            name = "main_menu_bg_1080p"
        elif actual_h <= 1440:
            name = "main_menu_bg_1440p"
        else:
            name = "main_menu_bg_2160p"
        return renpy.displayable(name), None


image main_menu_bg_720p:
    Movie(play="images/main_menu_bg_720p.webm", loop=True, start_image="images/cg/cg1.webp")
    zoom (2560 / 1280)

image main_menu_bg_1080p:
    Movie(play="images/main_menu_bg_1080p.webm", loop=True, start_image="images/cg/cg1.webp")
    zoom (2560 / 1920)

image main_menu_bg_1440p:
    Movie(play="images/main_menu_bg_1440p.webm", loop=True, start_image="images/cg/cg1.webp")
    zoom (2560 / 2560)

image main_menu_bg_2160p:
    Movie(play="images/main_menu_bg_2160p.webm", loop=True, start_image="images/cg/cg1.webp")
    zoom (2560 / 3840)

image main_menu_bg = DynamicDisplayable(select_menu_bg)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
