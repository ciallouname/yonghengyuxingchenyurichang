define achievement.steam_position = "bottom right"

label achievement(who):
    python:
        achievement.Sync()

        ach_id = f"NEW_1_{who}"
        achievement.register(ach_id, steam=f"NEW_ACHIEVEMENT_1_{who}")
        if not achievement.has(ach_id):
            achievement.grant(ach_id)

        achievement.sync()

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
