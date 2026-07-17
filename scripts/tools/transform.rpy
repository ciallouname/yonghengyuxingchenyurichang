transform show_roll(x=0.5):
    xcenter x
    yalign 1.1
    zoom 0.5

transform main_menu_show_btn(wait=0):
    xoffset 1000
    alpha 0
    pause wait
    easein 1 xoffset 0 alpha 1.0

transform main_menu_bg_transform:
    on show:
        alpha 0
        linear 1.0 alpha 1.0
    on replace:
        alpha 0
        linear 1.0 alpha 1.0

transform main_menu_char_bg_transform:
    on show:
        alpha 0
        pause 1.0
        linear 1.0 alpha 1.0
    on replace:
        alpha 0
        pause 1.0
        linear 1.0 alpha 1.0


init python:
    import pygame

label disable_user_interaction():
    python:



        pygame.event.set_blocked(pygame.MOUSEWHEEL)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)


        pygame.event.set_blocked(pygame.KEYDOWN)
        pygame.event.set_blocked(pygame.KEYUP)



        pygame.event.set_blocked(pygame.QUIT)

    return

label enable_user_interaction():


    python:
        pygame.event.set_allowed(pygame.MOUSEWHEEL)
        pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

        pygame.event.set_allowed(pygame.KEYDOWN)
        pygame.event.set_allowed(pygame.KEYUP)

        pygame.event.set_allowed(pygame.QUIT)

    return



init python:
    import math
    class Shaker(object):
        anchors = {
        'top' : 0.0,
        'center' : 0.5,
        'bottom' : 1.0,
        'left' : 0.0,
        'right' : 1.0,
        }
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            
            self.start = [ self.anchors.get(i, i) for i in start ]  
            self.dist = dist    
            self.child = child
        
        def __call__(self, t, sizes):
            
            
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            
            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):
        
        move = Shaker(start, child, dist=dist)
        
        return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

    Shake = renpy.curry(_Shake)





transform char_enter_left:
    xalign -0.21
    yalign 1.0
    linear 0.55 xalign 0.5

transform char_enter_right:
    xalign 0.86
    linear 0.55 xalign 0.5

transform char_exit_left:
    linear 0.35 xalign -2.0

transform char_exit_right:
    linear 0.35 xalign 3.0

transform emphasis_pop:
    zoom 1.0
    linear 0.12 zoom 1.06
    linear 0.12 zoom 1.0

transform shy_shrink:
    linear 0.12 zoom 0.94 yoffset 10
    pause 0.05
    linear 0.12 zoom 1.0 yoffset 0

transform lean_in:
    yoffset 0
    linear 0.18 yoffset -20
    linear 0.18 yoffset 0

transform bounce_small:
    yoffset 0
    linear 0.12 yoffset -12
    linear 0.18 yoffset 0

transform glare_shake:
    parallel:
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 xoffset 6
        linear 0.05 xoffset -6
        linear 0.05 xoffset 0


transform deny_shake_small:
    parallel:
        linear 0.04 xoffset 8
        linear 0.04 xoffset -8
        linear 0.04 xoffset 5
        linear 0.04 xoffset -5
        linear 0.04 xoffset 0

transform nod_small:
    yoffset 0
    linear 0.10 yoffset -10
    linear 0.12 yoffset 0

transform look_away_small:
    xoffset 0
    linear 0.15 xoffset 26 alpha 0.98
    linear 0.15 xoffset 0 alpha 1.0

transform turn_around:
    xoffset 0
    linear 0.3 xoffset 100
    linear 0.3 xoffset -100
    linear 0.3 xoffset 0



transform angry_stomp:

    yoffset 0
    linear 0.08 yoffset 15
    linear 0.06 yoffset 0
    pause 0.1
    linear 0.08 yoffset 15
    linear 0.06 yoffset 0

transform shocked_step_back:

    xoffset 0
    linear 0.15 xoffset -30
    pause 0.2
    linear 0.2 xoffset 0

transform excited_lean_forward:

    yoffset 0 zoom 1.0
    linear 0.2 yoffset 100 zoom 1.05

transform excited_lean_forward_undo:

    yoffset 100 zoom 1.05
    linear 0.2 yoffset 0 zoom 1.0

transform disappointed_droop:

    yoffset 0 alpha 1.0
    linear 0.3 yoffset 20 alpha 1.0



transform look_at_left:

    xoffset 0
    linear 0.15 xoffset -15

transform look_at_right:

    xoffset 0
    linear 0.15 xoffset 15

transform celebrate_jump:

    yoffset 0
    linear 0.15 yoffset -40
    linear 0.2 yoffset 5
    linear 0.1 yoffset 0



transform focus_speaker:

    zoom 1.0 alpha 1.0
    linear 0.2 zoom 1.03 alpha 1.0

transform unfocus_listener:

    zoom 1.0 alpha 1.0
    linear 0.2 zoom 0.98



transform shy_look_away:

    parallel:
        linear 0.12 zoom 0.94 yoffset 10
        pause 0.05
        linear 0.12 zoom 1.0 yoffset 0
    parallel:
        xoffset 0
        pause 0.1
        linear 0.15 xoffset 26 alpha 0.98
        linear 0.15 xoffset 0 alpha 1.0

transform angry_shake_stomp:

    parallel:
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 xoffset 6
        linear 0.05 xoffset -6
        linear 0.05 xoffset 0
    parallel:
        yoffset 0
        pause 0.25
        linear 0.08 yoffset 15
        linear 0.06 yoffset 0




transform bg_pan_left:
    subpixel True
    zoom 1.05
    xalign 1.0 yalign 0.5
    linear 20.0 xalign 0.0

transform bg_pan_right:
    subpixel True
    zoom 1.05
    xalign 0.0 yalign 0.5
    linear 20.0 xalign 1.0

transform bg_pan_up:
    subpixel True
    zoom 1.05
    xalign 0.5 yalign 1.0
    linear 20.0 yalign 0.0

transform bg_pan_down:
    subpixel True
    zoom 1.05
    xalign 0.5 yalign 0.0
    linear 20.0 yalign 1.0

transform bg_zoom_in:
    subpixel True
    zoom 1.0
    xalign 0.5 yalign 0.5
    linear 20.0 zoom 1.05

transform bg_zoom_out:
    subpixel True
    zoom 1.05
    xalign 0.5 yalign 0.5
    linear 20.0 zoom 1.0



transform letterbox_top(start_height=0, end_height=220, duration=2.0):
    xalign 0.5
    yalign 0.0
    ysize start_height
    easein duration ysize end_height

transform letterbox_bottom(start_height=0, end_height=220, duration=2.0):
    xalign 0.5
    yalign 1.0
    ysize start_height
    easein duration ysize end_height



transform consciousness_fade_out:
    blur 0
    parallel:
        linear 2.0 blur 25

define dis_master = { "master": Dissolve(0.5) }
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
