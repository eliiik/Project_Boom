# -*- coding:utf-8 -*-

import pyglet
from GameModules.resource import mouse


def on_mouse_press(x, y, button, modifiers):
    pass

def on_mouse_release(x, y, button, modifiers):
    pass

def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    pass

#使用自定义鼠标样式
cursor = pyglet.window.ImageMouseCursor(mouse, 16, 8)
