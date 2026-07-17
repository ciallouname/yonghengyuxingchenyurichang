


init -999 python:





    class SystemVoiceOnShiyu(Action):
        """
    开启时语音
    """
        
        def __call__(self):
            persistent.system_voice_shiyu = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.system_voice_shiyu

    class SystemVoiceOffShiyu(Action):
        """
    关闭时语音
    """
        
        def __call__(self):
            persistent.system_voice_shiyu = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not persistent.system_voice_shiyu

    class SystemVoiceOnXingmi(Action):
        """
    开启星弥语音
    """
        
        def __call__(self):
            persistent.system_voice_xingmi = True
            renpy.restart_interaction()
        
        def get_selected(self):
            return persistent.system_voice_xingmi

    class SystemVoiceOffXingmi(Action):
        """
    关闭星弥语音
    """
        
        def __call__(self):
            persistent.system_voice_xingmi = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return not persistent.system_voice_xingmi
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
