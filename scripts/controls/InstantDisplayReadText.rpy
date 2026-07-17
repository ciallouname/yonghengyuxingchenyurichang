


init -999 python:





    class InstantDisplayReadTextOn(Action):
        """
    开启瞬间显示已读文本
    """
        
        def __call__(self):
            persistent.instant_display_read_text = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.instant_display_read_text

    class InstantDisplayReadTextOff(Action):
        """
    关闭瞬间显示已读文本
    """
        
        def __call__(self):
            persistent.instant_display_read_text = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not persistent.instant_display_read_text
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
