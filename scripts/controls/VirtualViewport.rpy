



























init python:
    
    import math
    
    class VirtualContentViewport(renpy.display.layout.Container):
        """
        真正的虚拟化列表组件。

        与 VPGrid 的关键区别:
          - VPGrid: 在屏幕创建时实例化所有 child，render() 时跳过不可见的渲染
          - 本组件: 只在 render() 时按需创建可见+缓冲区的 child，其余不存在

        机制:
          - _cache: {index: Displayable} — 当前活跃的 Displayable 字典
          - render() 时根据 yadjustment.value 计算可见范围
          - 为新进入可见范围的条目调用 item_factory() 创建 Displayable
          - 移出缓冲区的条目从 _cache 中删除
          - 事件通过 Render 树的坐标变换自动转发到正确的子节点
        """
        
        _render_priority = 10  
        
        def __init__(
            self,
            data_source=None,
            item_factory=None,
            item_height=234,
            viewport_height=897,
            viewport_width=2084,
            buffer_items=3,
            yadjustment=None,
            xadjustment=None,
            yinitial=None,
            style="default",
            **properties,
        ):
            """
            `data_source`
                数据源列表（例如 _history_list）。

            `item_factory`
                工厂函数: (item) -> Displayable。接收数据项，返回对应的显示对象。
                返回 None 表示该项无法创建（会被跳过）。

            `item_height`
                每个条目的总高度（含间距），用于计算可见范围。

            `viewport_height`, `viewport_width`
                外层 Viewport 的尺寸，用于计算可见范围。

            `buffer_items`
                可见区域外额外保留的条目数，防止快速滚动时短暂空白。

            `yadjustment`, `xadjustment`
                滚动调整量。如果未提供，内部自动创建。

            `yinitial`
                外层 Viewport 的初始 Y 滚动位置 (0.0=顶, 1.0=底)。
                用于在 Viewport 修正 adjustment 值之前预先计算正确的可见范围。
            """
            super(VirtualContentViewport, self).__init__(style=style, **properties)
            
            self.data_source = data_source if data_source is not None else []
            self.item_factory = item_factory
            self.item_height = item_height
            self.viewport_height = viewport_height
            self.viewport_width = viewport_width
            self.buffer_items = buffer_items
            self._yinitial = yinitial
            
            
            if yadjustment is None:
                self.yadjustment = renpy.display.behavior.Adjustment(1, 0)
            else:
                self.yadjustment = yadjustment
            
            if xadjustment is None:
                self.xadjustment = renpy.display.behavior.Adjustment(0, 0)
            else:
                self.xadjustment = xadjustment
            
            if self.yadjustment.adjustable is None:
                self.yadjustment.adjustable = True
            if self.xadjustment.adjustable is None:
                self.xadjustment.adjustable = True
            
            
            self._cache = {}
            
            
            self._last_first = -1
            self._last_last = -1
            
            
            self._last_data_len = -1
            
            
            self._predicted = False
        
        
        
        def set_data_source(self, new_data):
            """
            更新数据源并在变化时清空缓存。
            在屏幕显示前调用以确保反映最新的 _history_list。
            """
            new_data = new_data if new_data is not None else []
            if new_data is not self.data_source or len(new_data) != self._last_data_len:
                self._cache.clear()
                self.children = []
                self.child = None
                self._last_first = -1
                self._last_last = -1
                self._predicted = False
            self.data_source = new_data
            self._last_data_len = len(new_data)
            renpy.display.render.redraw(self, 0)
        
        def refresh(self):
            """强制刷新缓存（在数据内容变化但长度不变时使用）。"""
            self._cache.clear()
            self.children = []
            self.child = None
            self._last_first = -1
            self._last_last = -1
            self._predicted = False
            renpy.display.render.redraw(self, 0)
        
        def reset_scroll(self):
            """滚动到列表末尾（对应 yinitial 1.0 的行为）。"""
            yrange = max(
                len(self.data_source) * self.item_height - self.viewport_height, 0
            )
            self.yadjustment.range = yrange
            self.yadjustment.page = self.viewport_height
            self.yadjustment.value = yrange
            self.yadjustment.update()
        
        
        
        def _get_visible_range(self):
            """
            根据滚动位置计算可见范围（含缓冲区）。
            返回 (first_visible_index, last_visible_index)。
            """
            total = len(self.data_source)
            if total == 0:
                return 0, 0
            
            scroll_y = int(self.yadjustment.value)
            h = self.item_height
            vh = self.viewport_height
            buf = self.buffer_items
            
            first = max(0, scroll_y // h - buf)
            last = min(total, (scroll_y + vh) // h + buf + 1)
            
            return first, last
        
        def _update_cache(self, first, last):
            """
            更新 _cache:
              - 为 [first, last) 范围内缺失的条目创建 Displayable
              - 移除不再需要的条目
              - 同步 self.children 以支持 Container 的事件转发
            """
            visible = set(range(first, last))
            
            
            to_remove = [idx for idx in self._cache if idx not in visible]
            for idx in to_remove:
                del self._cache[idx]
            
            
            for idx in sorted(visible):
                if idx not in self._cache:
                    try:
                        item = self.data_source[idx]
                        d = self.item_factory(item)
                        self._cache[idx] = d  
                    except Exception:
                        if renpy.config.developer:
                            import traceback
                            traceback.print_exc()
                        self._cache[idx] = None
            
            
            self.children = [c for c in self._cache.values() if c is not None]
            if self.children:
                self.child = self.children[-1]
        
        def _preload_both_ends(self):
            """
            预创建并预加载首尾各一页的条目。
            这样无论 yinitial 是 0.0 还是 1.0，首帧都能立刻显示内容。
            """
            total = len(self.data_source)
            if total == 0:
                return
            
            step = self.item_height
            vh = self.viewport_height
            buf = self.buffer_items
            page_count = max(1, vh // step + 1 + buf)
            
            
            for idx in range(min(total, page_count)):
                self._ensure_item(idx)
            
            
            start = max(0, total - page_count)
            for idx in range(start, total):
                self._ensure_item(idx)
        
        def _ensure_item(self, idx):
            """
            确保条目 idx 已创建并已注册图片预测。
            如果已在缓存中则跳过，否则调用工厂函数创建并预测。
            """
            if idx in self._cache:
                d = self._cache[idx]
            else:
                try:
                    d = self.item_factory(self.data_source[idx])
                    self._cache[idx] = d
                except Exception:
                    self._cache[idx] = None
                    return
            
            if d is not None:
                renpy.display.predict.displayable(d)
        
        
        
        def per_interact(self):
            """注册 adjustment，使惯性滚动和动画正常工作。"""
            self.yadjustment.register(self)
            self.xadjustment.register(self)
        
        def render(self, width, height, st, at):
            rv_width = self.viewport_width or width
            rv_height = self.viewport_height or height
            
            total_items = len(self.data_source)
            
            
            if total_items == 0:
                self.yadjustment.range = 0
                self.yadjustment.page = rv_height
                self.yadjustment.update()
                rv = renpy.display.render.Render(rv_width, rv_height)
                return rv
            
            step = self.item_height
            total_height = total_items * step
            
            
            yrange = max(total_height - rv_height, 0)
            
            if (
                self.yadjustment.range != yrange
                or self.yadjustment.page != rv_height
            ):
                self.yadjustment.range = yrange
                self.yadjustment.page = rv_height
                self.yadjustment.update()
            
            
            
            
            if self._yinitial is not None:
                if isinstance(self._yinitial, float):
                    initial_value = yrange * self._yinitial
                else:
                    initial_value = int(self._yinitial)
                self.yadjustment.value = initial_value
                self._yinitial = None  
            
            
            redraw = self.yadjustment.periodic(st)
            if redraw is not None:
                renpy.display.render.redraw(self, redraw)
            
            
            first, last = self._get_visible_range()
            
            if (first != self._last_first) or (last != self._last_last):
                self._update_cache(first, last)
                self._last_first = first
                self._last_last = last
            
            
            
            
            rv = renpy.display.render.Render(rv_width, total_height)
            
            scroll_y = int(self.yadjustment.value)
            
            for idx, child in list(self._cache.items()):
                if child is None:
                    continue
                
                item_y = idx * step
                screen_y = item_y - scroll_y
                
                
                if screen_y + step < 0 or screen_y >= rv_height:
                    continue
                
                try:
                    surf = renpy.display.render.render(
                        child, rv_width, step, st, at
                    )
                    
                    
                    child.place(rv, 0, item_y, rv_width, step, surf)
                except Exception:
                    if renpy.config.developer:
                        import traceback
                        traceback.print_exc()
                    
                    if idx in self._cache:
                        del self._cache[idx]
            
            return rv
        
        def event(self, ev, x, y, st):
            """
            将事件转发给命中的缓存子节点。

            (x, y) 是内容空间坐标 — Viewport 的 subsurface/blit 变换
            已自动应用了滚动偏移。

            仅处理我们未处理的通用事件；鼠标滚轮和拖拽由外层 Viewport 处理。
            """
            step = self.item_height
            idx = int(y // step)
            
            if 0 <= idx < len(self.data_source):
                child = self._cache.get(idx)
                if child is not None:
                    local_x = x
                    local_y = y - idx * step
                    
                    result = child.event(ev, local_x, local_y, st)
                    if result is not None:
                        return result
            
            return None
        
        def _handles_event(self, event):
            """
            检查缓存中的子节点是否处理此事件。
            对焦点系统和悬停检测很重要。
            """
            for child in self._cache.values():
                if child is not None and child._handles_event(event):
                    return True
            return False
        
        def visit(self):
            """
            返回所有活跃子节点的列表。
            供 Ren'Py 的 visit_all（预测）、焦点遍历等使用。
            """
            return [c for c in self._cache.values() if c is not None]
        
        def predict_one(self):
            """
            预测所有条目的图像到后台预加载队列。

            核心设计: 使用 Ren'Py 内置的 predict.displayable() 遍历
            Displayable 树来发现所有需要预加载的图像节点。对于层叠式
            图像（LayeredImageProxy），predict.displayable() 会正确触发
            ImageReference.find_target() → LayeredImage._duplicate() →
            Fixed(各层图像) → 递归预测每一层。

            关键:
              - 不创建 item_factory 的完整 Fixed 树（不破坏虚拟化）
              - 按图像名去重：同一角色 + 同一表情只合成一次层叠图像
              - 普通 ImageBase 直接传给 cache.preload_image()
              - 图像解码在后台 preload 线程异步进行
            """
            total = len(self.data_source)
            if total == 0 or self._predicted:
                return
            
            self._predicted = True
            
            
            self._preload_image_name("log_data_bg")
            self._preload_image_file("gui/custom2/system/history/log_data_bo_jumpback_normal.png")
            self._preload_image_file("gui/custom2/system/history/log_data_bo_jumpback_click.png")
            self._preload_image_file("gui/custom2/dialog/dialog_menu_revoice_normal.png")
            self._preload_image_file("gui/custom2/dialog/dialog_menu_revoice_click.png")
            
            
            seen_side_images = set()
            
            for idx in range(total):
                item = self.data_source[idx]
                side = item.side_image
                if side is None:
                    continue
                
                
                key = side.name if hasattr(side, "name") else id(side)
                if key in seen_side_images:
                    continue
                seen_side_images.add(key)
                
                
                
                
                
                
                
                
                
                
                renpy.display.predict.displayable(side)
        
        
        
        @staticmethod
        def _preload_image_name(name):
            """通过注册图像名预加载（含层叠式图像自动处理）。"""
            d = renpy.display.image.images.get(tuple(name.split()))
            if d is not None:
                renpy.display.predict.displayable(d)
        
        @staticmethod
        def _preload_image_file(filename):
            """通过文件名预加载。构造 ImageBase 键直接加入预加载队列。"""
            renpy.display.im.cache.preload_image(
                renpy.display.im.Image(str(filename))
            )
        
        def _predict_item(self, idx):
            """为单个索引创建 Displayable（如果尚未缓存）并预测其图像。"""
            if idx in self._cache:
                d = self._cache[idx]
            else:
                try:
                    d = self.item_factory(self.data_source[idx])
                    self._cache[idx] = d
                except Exception:
                    self._cache[idx] = None
                    return
            
            if d is not None:
                renpy.display.predict.displayable(d)
    
    
    
    
    
    
    
    
    
    def _make_history_entry_displayable(h):
        """
        根据 HistoryEntry 对象创建 Displayable 树。

        等价于原来的 screen history_entry(h) 加上各子元素。
        返回 Fixed 容器，包含: 背景图、(可选)侧边图、说话者、内容、按钮。
        """
        from renpy.display.layout import Fixed, Crop
        from renpy.display.image import ImageReference
        from renpy.display.transform import Transform
        from renpy.display.text import Text
        from renpy.display.behavior import ImageButton
        
        
        entry = Fixed(style="history_entry_frame")
        
        
        
        bg = renpy.easy.displayable("log_data_bg")
        entry.add(bg)
        
        
        if h.side_image is not None:
            if h.image_tag == "xm":
                crop_rect = (80, 360, 765, 180)
            elif h.image_tag == "syq_":
                crop_rect = (20, 100, 765, 180)
            else:
                crop_rect = (80, 292, 765, 180)
            
            try:
                
                ref = ImageReference(h.side_image)
                cropped = Crop(crop_rect, ref)
                
                t = Transform(
                    child=cropped,
                    zoom=1.1,
                    yalign=1.0,
                    yoffset=-990,
                    xoffset=-300,
                )
                entry.add(t)
            except Exception:
                
                pass
        
        
        if h.who:
            who_text = Text(
                h.who,
                style="history_who_text",
                substitute=False,
            )
            entry.add(who_text)
        
        
        what_filtered = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
        what_text = Text(
            what_filtered,
            style="history_what_text",
            substitute=False,
        )
        entry.add(what_text)
        
        
        
        
        
        
        can_rollback = renpy.get_identifier_checkpoints(h.rollback_identifier) is not None
        
        if h.voice.filename is not None:
            
            if can_rollback:
                jumpback = ImageButton(
                    idle_image="gui/custom2/system/history/log_data_bo_jumpback_normal.png",
                    hover_image="gui/custom2/system/history/log_data_bo_jumpback_click.png",
                    style="history_jumpback_button",
                    activate_sound=_history_activate_sound,
                    hover_sound=_history_hover_sound,
                    clicked=Confirm(
                        "确定要跳转到该处吗？",
                        yes=RollbackToIdentifier(h.rollback_identifier),
                        no=None,
                        confirm_selected=False,
                    ),
                )
                entry.add(jumpback)
            
            revoice = ImageButton(
                idle_image="gui/custom2/dialog/dialog_menu_revoice_normal.png",
                hover_image="gui/custom2/dialog/dialog_menu_revoice_click.png",
                style="history_revoice_button",
                clicked=PlayCharacterVoice(
                    "xingmi" if h.image_tag == "xm" else "shiyu",
                    h.voice.filename,
                    selected=True,
                ),
            )
            entry.add(revoice)
        else:
            
            if can_rollback:
                jumpback = ImageButton(
                    idle_image="gui/custom2/system/history/log_data_bo_jumpback_normal.png",
                    hover_image="gui/custom2/system/history/log_data_bo_jumpback_click.png",
                    style="history_jumpback_button_no_voice",
                    activate_sound=_history_activate_sound,
                    hover_sound=_history_hover_sound,
                    clicked=Confirm(
                        "确定要跳转到该处吗？",
                        yes=RollbackToIdentifier(h.rollback_identifier),
                        no=None,
                        confirm_selected=False,
                    ),
                )
                entry.add(jumpback)
        
        return entry
    
    
    
    
    def create_history_virtual_viewport(yadjustment=None):
        """
        创建为历史屏幕配置好的 VirtualContentViewport。

        在 screen 的 default 语句中使用:
            default history_vc = create_history_virtual_viewport(adj)
        """
        return VirtualContentViewport(
            data_source=_history_list,
            item_factory=_make_history_entry_displayable,
            item_height=234,        
            viewport_height=897,
            viewport_width=2084,
            buffer_items=3,
            yadjustment=yadjustment,
            yinitial=1.0,           
        )

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
