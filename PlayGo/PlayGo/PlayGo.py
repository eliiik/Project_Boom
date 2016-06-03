#!/usr/bin/python
# -*- coding:utf-8 -*-

import pyglet
from pyglet.window import mouse
from GamePlay.GameModules import frame, resource, box, loadobj, fx
from GamePlay import control

gameWindow = pyglet.window.Window(800, 600)
gameWindow.set_icon(resource.icon1, resource.icon2)
#初始化游戏状态
score = 0
leftTimes = 120

mainBatch = pyglet.graphics.Batch()
frameBatch = pyglet.graphics.Batch()
boxBatch = pyglet.graphics.Batch()
boardBatch = pyglet.graphics.Batch()
wordBatch = pyglet.graphics.Batch()

wall = frame.Frame(resource.wall,400,300,batch = frameBatch)
bg = frame.Frame(resource.bg, 400,300,batch = mainBatch)
score = frame.Scoreboard("Score: ", 100, 550, wordBatch)
scoreBoard = frame.Frame(resource.scoreboard, 100, 550, boardBatch)
gameWindow.set_mouse_cursor(control.cursor)

boxes = loadobj.boxes(batch = boxBatch)
boom = fx.boxBoom()

gameWindow.push_handlers(boxes[1].mouseHandler)
leftButtom = pyglet.window.mouse.LEFT
#mouse
#@gameWindow.on_mouse_drag(y, dx, dy, leftButtom)
#def printouse():
#    print "pressed"

@gameWindow.event

def on_draw():

    gameWindow.clear()

    mainBatch.draw()
    frameBatch.draw()
    boxBatch.draw()
    boardBatch.draw()
    wordBatch.draw()

   # boom.draw()

#def on_mouse_motion(x, y, dx, dy):
#    print "x: ",x, " y: ", y, " dx: ", dx, " dy: ", dy
def on_key_press():
    print "pressedKey"
def on_mouse_motion():
    print "pressed"

def on_mouse_release():
    print "released"

def update(dt):
    victory = False
    boxes[1]
    #for obj in boxes:
    #    obj.update(dt)


if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()