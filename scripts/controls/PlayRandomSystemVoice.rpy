


init -999 python:
    import random




















    system_voice_scene_groups = [
    [],         
    [1],     
    [3],     
    [5],     
    [7],     
    [9],    
    [11, 12],   
    [13],   
    [15],       
    [16],       
    [17],       
    [18],       
    [19],       
]



    system_voice_versions_shiyu = [
    0,  
    4,  
    1,  
    4,  
    1,  
    4,  
    1,  
    4,  
    1,  
    4,  
    2,  
    1,  
    1,  
    4,  
    1,  
    2,  
    1,  
    1,  
    1,  
    1,  
]



    system_voice_versions_xingmi = [
    0,  
    3,  
    2,  
    3,  
    1,  
    3,  
    1,  
    3,  
    1,  
    3,  
    1,  
    1,  
    1,  
    3,  
    1,  
    2,  
    1,  
    1,  
    1,  
    1,  
]

    class PlayRandomSystemVoice(Action):
        """
    随机播放系统语音
    
    参数:
        scene_group: 场景组编号（1-12）
            1: 点击设置按钮
            2: 点击画廊
            3: 点击音声鉴赏
            4: 点击立绘鉴赏
            5: 点击读取存档
            6: 点击语音测试
            7: 点击退出游戏
            8: 启动游戏-制作组
            9: 启动游戏-游戏名
            10: 新游戏
            11: 继续游戏
            12: 保存
        channel: 播放通道，默认为 "voice"
    
    行为:
        1. 根据 persistent.system_voice_shiyu 和 persistent.system_voice_xingmi 判断哪些角色可用
        2. 从可用角色中随机选择一个
        3. 根据场景组，随机选择组内的一个场景编号
        4. 根据数组中指定的固定版本号播放语音
    """
        
        def __init__(self, scene_group, channel="voice"):
            self.scene_group = scene_group
            self.channel = channel
        
        def __call__(self):
            
            if self.scene_group < 1 or self.scene_group > 12:
                return
            
            
            available_characters = []
            
            if persistent.system_voice_shiyu:
                available_characters.append("shiyu")
            
            if persistent.system_voice_xingmi:
                available_characters.append("xingmi")
            
            
            if not available_characters:
                return
            
            
            selected_character = random.choice(available_characters)
            
            
            scenes = system_voice_scene_groups[self.scene_group]
            scene_id = random.choice(scenes)
            
            
            if selected_character == "shiyu":
                version = system_voice_versions_shiyu[scene_id]
                prefix = "C"
            else:  
                version = system_voice_versions_xingmi[scene_id]
                prefix = "D"
            
            
            
            voice_file = "audio/system/{}{}-{}.ogg".format(prefix, scene_id, version)
            
            
            renpy.sound.play(voice_file, channel=self.channel)
            
            renpy.restart_interaction()
        
        def get_sensitive(self):
            """
        判断按钮是否可用
        如果两个角色的系统语音都被关闭，则按钮不可用
        """
            return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
