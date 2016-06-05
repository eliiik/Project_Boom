#!/usr/bin/python
# -*- coding:utf-8 -*-

import pyglet
from pyglet.window import mouse, key
from GamePlay.GameModules import frame, resource, gamebox, loadobj, fx, gamemap
from GamePlay import control
mouseMove = [0,0,0,0]
gameWindow = pyglet.window.Window(800, 600)
gameWindow.set_icon(resource.icon1, resource.icon2)
#初始化游戏状态
score = 0
leftTimes = 120

mainBatch = pyglet.graphics.Batch()
frameBatch = pyglet.graphics.Batch()

boardBatch = pyglet.graphics.Batch()
wordBatch = pyglet.graphics.Batch()

wall = frame.Frame(resource.wall,400,300,batch = frameBatch)
bg = frame.Frame(resource.bg, 400,300,batch = mainBatch)
score = frame.Scoreboard("Score: ", 100, 550, wordBatch)
scoreBoard = frame.Frame(resource.scoreboard, 100, 550, boardBatch)
#gameWindow.set_mouse_cursor(resource.cursor)


boom = fx.boxBoom()

fps_display = pyglet.clock.ClockDisplay()

leftButtom = pyglet.window.mouse.LEFT
@gameWindow.event

def on_mouse_press(x, y, buttons, modifiers):

    mouseMove[0] = x
    mouseMove[2] = y


@gameWindow.event
def on_mouse_release(x, y, buttons, modifiers):
    mouseMove[1] = x
    mouseMove[3] = y
    print mouseMove
    control.mouseCoord(*mouseMove)
    control.mouseDrag(*mouseMove)
    
def on_key_press(symbol, modifiers):
    print symbol

@gameWindow.event

def on_draw():

    gameWindow.clear()

    mainBatch.draw()
    frameBatch.draw()
    loadobj.boxBatch.draw()
    boardBatch.draw()
    wordBatch.draw()
    fps_display.draw()
   # boom.draw()


def update(dt):
    victory = False
    #for obj in boxes:
    #    obj.update(dt)


if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()
