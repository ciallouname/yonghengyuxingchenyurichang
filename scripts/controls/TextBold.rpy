


init -999 python:





    class TextBoldOn(Action):
        """
    开启文本加粗
    """
        
        def __call__(self):
            persistent.text_bold = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.text_bold

    class TextBoldOff(Action):
        """
    关闭文本加粗
    """
        
        def __call__(self):
            persistent.text_bold = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not persistent.text_bold
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
