# -*- coding:utf-8 -*-
import pyglet
import utils
import gamebox

#资源路径
pyglet.resource.path = ["GameResource"]
pyglet.resource.reindex()

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
boxList = [box1,box2,box3,box4]
for i in range(len(boxList)):
    boxList[i].width = boxList[i].height = gamebox.Box.BOXSIZE
utils.centerImage(*boxList)

#特效爆炸
boom = pyglet.resource.image("Explosion.png")
utils.centerImage(boom)

#鼠标样式
#mouseCurser = pyglet.resource.image("Mouse.png")
#cursor = pyglet.window.ImageMouseCursor(mouseCurser, 16, 8)

#图标样式
iconfile1 = open("GameResource\\16.png", 'rb')
iconfile2 = open("GameResource\\32.png", 'rb')

icon1 = pyglet.image.load("icon1", file = iconfile1)
icon2 = pyglet.image.load("icon2", file = iconfile2)