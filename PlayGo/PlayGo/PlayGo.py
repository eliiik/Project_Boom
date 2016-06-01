#!/usr/bin/python
# -*- coding:utf-8 -*-

import pyglet
from GamePlay.GameModules import resource, box, loadobj

#新建窗口
gameWindow = pyglet.window.Window(800, 600)
gameWindow.set_minimum_size(240, 180)
#初始化游戏状态
score = 0
leftTimes = 120

mainBatch = pyglet.graphics.Batch()


def createBox():
    boxes = loadobj.boxes(batch = mainBatch)

@gameWindow.event

def on_draw():
    windowWidth = gameWindow.width
    windowHeight = gameWindow.height
    frame = pyglet.sprite.Sprite(img = resource.frame, x = windowWidth//2, y = windowHeight//2)

    createBox()
    gameWindow.clear()

    resource.bg.blit(windowWidth//2, windowHeight//2,0)
    frame.draw()
    mainBatch.draw()

def update(dt):
    victory = False


if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()