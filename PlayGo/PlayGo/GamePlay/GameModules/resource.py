# -*- coding:utf-8 -*-
import pyglet
import utils
import gamebox
import gamemap

#资源路径
pyglet.resource.path = ["GameResource"]
pyglet.resource.reindex()

#背景
bg = pyglet.resource.image("Background.png")
utils.centerImage(bg)

wall = pyglet.resource.image("Frame.png")
utils.centerImage(wall)

#地图
map1 = pyglet.resource.image("Map1.png")
map2 = pyglet.resource.image("Map2.png")
mapList = [map1, map2]
for i in mapList:
    i.width = i.height = 468
    utils.centerImage(i)

#按键
startButton = pyglet.resource.image("startButton-129,112.png")
utils.centerImage(startButton)
pauseButton = pyglet.resource.image("pauseButton-129,112.png")
utils.centerImage(pauseButton)
exitButton = pyglet.resource.image("exitButton-221,112.png")
utils.centerImage(exitButton)

#板
scoreboard = pyglet.resource.image("scoreBoard-224,496.png")
stepBoard = pyglet.resource.image("stepBoard-174,275.png")
utils.centerImage(stepBoard)
exitBoard = pyglet.resource.image("exitBoard-400,300.png")
utils.centerImage(exitBoard)
nextLevel = pyglet.resource.image("nextBoard-400,300.png")
utils.centerImage(nextLevel)
gameover = pyglet.resource.image("gameover-400,350.png")
utils.centerImage(gameover)



#数字
number0 = pyglet.resource.image("0.png")
number1 = pyglet.resource.image("1.png")
number2 = pyglet.resource.image("2.png")
number3 = pyglet.resource.image("3.png")
number4 = pyglet.resource.image("4.png")
number5 = pyglet.resource.image("5.png")
number6 = pyglet.resource.image("6.png")
number7 = pyglet.resource.image("7.png")
number8 = pyglet.resource.image("8.png")
number9 = pyglet.resource.image("9.png")
numberList = [number0,number1,number2,number3,number4,
              number5,number6,number7,number8,number9]
for i in numberList:
    i.width = i.height = gamemap.NUMBERSIZE
utils.centerImage(*numberList)

#方块
box1 = pyglet.resource.image("Box1.png")
box2 = pyglet.resource.image("Box2.png")
box3 = pyglet.resource.image("Box3.png")
box4 = pyglet.resource.image("Box4.png")
box5 = pyglet.resource.image("Box5.png")
boxList = [box1,box2,box3,box4,box5]
for i in boxList:
    i.width = i.height = gamebox.Box.BOXSIZE
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