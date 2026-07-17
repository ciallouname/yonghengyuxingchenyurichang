


init -999 python:





    class SkipAfterChoicesOn(Action):
        """
    开启选项后快进
    """
        
        def __call__(self):
            preferences.skip_after_choices = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return preferences.skip_after_choices

    class SkipAfterChoicesOff(Action):
        """
    关闭选项后快进
    """
        
        def __call__(self):
            preferences.skip_after_choices = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not preferences.skip_after_choices
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
