


init -999 python:





    class AutoAfterChoicesOn(Action):
        """
    开启选项后继续自动前进
    """
        
        def __call__(self):
            persistent.auto_after_choices = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.auto_after_choices

    class AutoAfterChoicesOff(Action):
        """
    关闭选项后继续自动前进
    """
        
        def __call__(self):
            persistent.auto_after_choices = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not persistent.auto_after_choices

label AutoAfterChoicesCheckReset():
    if preferences.afm_enable and persistent.auto_after_choices == False:
        $ preferences.afm_enable = False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
