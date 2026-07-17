


init -999 python:





    class Continue(Action):
        """
    加载最新一个存档
    """
        
        def __call__(self):
            
            
            
            newest_page, newest_name = self.get_newest_slot()
            
            
            
            FileLoad(newest_name, confirm=False, page=newest_page)()
        
        def get_sensitive(self):
            
            
            if not renpy.newest_slot():
                return False
            
            newest_page, newest_name = self.get_newest_slot()
            
            
            
            if newest_page == '_reload':
                return False
            
            
            
            return FileLoadable(newest_name, page=newest_page)
        
        def get_newest_slot(self):
            """
        返回最新存档的页面和槽位
        """
            newest = renpy.newest_slot()
            
            if newest:
                page, name = newest.split("-")
                return page, name
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
