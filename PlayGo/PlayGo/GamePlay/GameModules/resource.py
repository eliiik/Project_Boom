# -*- coding:utf-8 -*-
import pyglet
import utils



#资源路径
pyglet.resource.path = ["GameResource"]
pyglet.resource.reindex()
pyglet.image.

#背景
bg = pyglet.resource.image("Background.jpg")
utils.centerImage(bg)

wall = pyglet.resource.image("Frame.png")
utils.centerImage(wall)

#计分板
scoreboard = pyglet.resource.image("Scoreboard.png")
utils.centerImage(scoreboard)

#方块
box1 = pyglet.resource.image("Box1.png")
box2 = pyglet.resource.image("Box2.png")
box3 = pyglet.resource.image("Box3.png")
box4 = pyglet.resource.image("Box4.png")
boxTuple = (box1,box2,box3,box4)
utils.centerImage(*boxTuple)

#特效爆炸
boom = pyglet.resource.image("Explosion.png")
utils.centerImage(boom)

#鼠标样式
mouseCurser = pyglet.resource.image("Mouse.png")

#图标样式
icon1 = pyglet.resource.image('16.png')
icon2 = pyglet.resource.image('32.png')
pyglet.image.load(