


init -999 python:





    class TextOutlineOn(Action):
        """
    开启文本描边
    """
        
        def __call__(self):
            persistent.text_outline = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.text_outline

    class TextOutlineOff(Action):
        """
    关闭文本描边
    """
        
        def __call__(self):
            persistent.text_outline = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not persistent.text_outline
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
