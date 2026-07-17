






init -900 python:
    
    
    import os as _os
    
    
    _compat_cache = {}
    
    _compat_mtime = {}
    
    
    def _try_validate_save(slotname):
        """
        读取并验证存档文件，检查其引用的脚本节点是否仍然存在。
        该函数复现了 Ren'Py 内部 RollbackLog.can_rollback() 的验证逻辑，
        但不会修改任何游戏状态。

        返回值：
            True  - 存档中至少有一个有效的回滚检查点，可以安全加载
            False - 所有检查点引用的脚本节点均已失效，加载必定崩溃
            None  - 无法判断（存档不存在、读取失败等）
        """
        try:
            
            
            log_data, signature = renpy.loadsave.location.load(slotname)
            
            if log_data is None:
                return None
            
            
            from renpy.compat.pickle import loads as _pickle_loads
            roots, log = _pickle_loads(log_data)
            
            
            
            
            if not hasattr(log, 'log'):
                return None
            
            for rb in reversed(log.log):
                if hasattr(rb, 'context') and hasattr(rb.context, 'current'):
                    if renpy.game.script.has_label(rb.context.current):
                        return True
            
            
            return False
        
        except Exception:
            
            return False
    
    
    def _is_save_compatible(slot, page=None):
        """
        检查指定存档槽位是否与当前脚本兼容。
        带缓存机制，根据存档文件修改时间判断是否需要重新检测。

        参数：
            slot  - 槽位号（如 1-8）
            page  - 页面号（如 "1", "auto" 等）

        返回值同 _try_validate_save()
        """
        if page is not None:
            slotname = "{}-{}".format(page, slot)
        else:
            slotname = str(slot)
        
        
        mtime = renpy.loadsave.slot_mtime(slotname)
        
        if mtime is None:
            
            _compat_cache.pop(slotname, None)
            _compat_mtime.pop(slotname, None)
            return None
        
        if slotname in _compat_cache and _compat_mtime.get(slotname) == mtime:
            return _compat_cache[slotname]
        
        result = _try_validate_save(slotname)
        _compat_cache[slotname] = result
        _compat_mtime[slotname] = mtime
        return result
    
    
    class SafeFileAction(Action):
        """
        包装 FileAction，在加载不兼容存档前弹出提示对话框。
        保存操作不受影响。
        """
        
        def __init__(self, slot, page=None):
            self.slot = slot
            self.page = page
            self._file_action = FileAction(slot)
        
        def __call__(self):
            
            if renpy.current_screen().screen_name[0] == "save":
                self._file_action()
                return
            
            
            page = self.page or persistent._file_page or "1"
            compat = _is_save_compatible(self.slot, page)
            
            if compat is False:
                
                renpy.run(
                    Confirm(
                        _("该存档与当前版本不兼容，无法加载。"),
                        Hide("confirm"),
                    )
                )
            else:
                
                self._file_action()
        
        def get_sensitive(self):
            return self._file_action.get_sensitive()
        
        def get_selected(self):
            return self._file_action.get_selected()
    
    
    class SafeContinue(Action):
        """
        加载最新存档，加载前自动检测兼容性。
        如果存档不兼容则弹出提示对话框。
        """
        
        def __call__(self):
            newest_page, newest_name = self._get_newest_slot()
            
            compat = _is_save_compatible(newest_name, newest_page)
            
            if compat is False:
                renpy.run(
                    Confirm(
                        _("该存档与当前版本不兼容，无法加载。"),
                        Hide("confirm"),
                    )
                )
            else:
                FileLoad(newest_name, confirm=False, page=newest_page)()
        
        def get_sensitive(self):
            if not renpy.newest_slot():
                return False
            
            newest_page, newest_name = self._get_newest_slot()
            
            if newest_page == '_reload':
                return False
            
            return FileLoadable(newest_name, page=newest_page)
        
        def _get_newest_slot(self):
            newest = renpy.newest_slot()
            if newest:
                page, name = newest.split("-")
                return page, name

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
