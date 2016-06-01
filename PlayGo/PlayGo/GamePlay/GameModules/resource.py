# -*- coding:utf-8 -*-
import pyglet
import utils



#资源路径
pyglet.resource.path = ["GameResource"]
pyglet.resource.reindex()

#背景
bg = pyglet.resource.image("Background.jpg")
utils.centerImage(bg)

frame = pyglet.resource.image("Frame.png")
utils.centerImage(frame)

#方块
box = pyglet.resource.image("Box.png")
utils.centerImage(box)