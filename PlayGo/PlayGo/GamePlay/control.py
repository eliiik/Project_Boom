# -*- coding:utf-8 -*-

import pyglet
from pyglet.window import mouse
from GameModules.resource import mouseCurser

def on_mouse_press(x, y, button, modifiers):
    pass

def on_mouse_release(x, y, button, modifiers):
    pass

def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & mouse.LEFT:
        return True

#使用自定义鼠标样式
cursor = pyglet.window.ImageMouseCursor(mouseCurser, 16, 8)
