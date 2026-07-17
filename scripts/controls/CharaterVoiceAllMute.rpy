


init -999 python:





    class CharaterVoiceAllMuteShiyu(Action):
        """
    开启时语音
    """
        
        def __call__(self):
            if "shiyu" in persistent._voice_mute and persistent.system_voice_shiyu == False:
                persistent._voice_mute.remove("shiyu")
                persistent.system_voice_shiyu = True
            else:
                persistent._voice_mute.add("shiyu")
                persistent.system_voice_shiyu = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return "shiyu" in persistent._voice_mute and persistent.system_voice_shiyu == False

    class CharaterVoiceAllMuteXingmi(Action):
        """
    关闭时语音
    """
        
        def __call__(self):
            if "xingmi" in persistent._voice_mute and persistent.system_voice_xingmi == False:
                persistent._voice_mute.remove("xingmi")
                persistent.system_voice_xingmi = True
            else:
                persistent._voice_mute.add("xingmi")
                persistent.system_voice_xingmi = False
            renpy.restart_interaction()
        
        def get_selected(self):
            return "xingmi" in persistent._voice_mute and persistent.system_voice_xingmi == False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
