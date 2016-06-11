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
start = 0
pause = 0
end = 0

mainBatch = pyglet.graphics.Batch()
mapBatch = pyglet.graphics.Batch()

boardBatch = pyglet.graphics.Batch()
wordBatch = pyglet.graphics.Batch()
buttomBatch = pyglet.graphics.Batch()
blockBatch = pyglet.graphics.Batch()

exitBatch = pyglet.graphics.Batch()

map1 = frame.Frame(resource.map1,533, 300,batch = mapBatch)
map1Block = frame.Frame(resource.map1,533, 300,batch = blockBatch)

map2 = frame.Frame(resource.map2,533, 300,batch = mapBatch)
map2Block = frame.Frame(resource.map2,533, 300,batch = blockBatch)
map2.visible = map2Block.visible = 0

bg = frame.Frame(resource.bg,400, 300, batch = mainBatch)
score = frame.Scoreboard("Score: ",128,450, wordBatch)
scoreBoard = frame.Frame(resource.scoreboard, 0, 391, boardBatch)
stepBoard = frame.Frame(resource.stepBoard,174,275,boardBatch)


pauseButton = frame.Frame(resource.pauseButton, 129,112, batch = buttomBatch)
pauseButton.visible = 0
startButton = frame.Frame(resource.startButton, 129,112, batch = buttomBatch)
exitButton = frame.Frame(resource.exitButton, 221,112, batch = buttomBatch)
exitBoard = frame.Frame(resource.exitBoard,400,300, batch = exitBatch)
exitBoard.visible = 0
aStep = frame.Frame(frame.numberDict[2], 1,0, batch = frame.numberBatch)
bStep = frame.Frame(frame.numberDict[3], 200,300, batch = frame.numberBatch)
#计数部分

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
    global start, pause, exitBoard, end, map1Block, map2Block
    mouseMove[1] = x
    mouseMove[3] = y
    if x in xrange(107, 151) and y in xrange(90, 134):
        if start:
            pause = 1
            startButton.visible = 1
            pauseButton.visible = 0
            start = 0
            map1Block.visible = 1
        else:
            for i in loadobj.boxes.allBoxes:
                i.visible = 1
            start = 1
            pause = 0
            startButton.visible = 0
            pauseButton.visible = 1
            map1Block.visible = 0


    if x in xrange(199,243) and y in xrange(90,134):
        exitBoard.visible = 1
        end = 1

    if end == 1:
        if x in xrange(320,368) and y in xrange(255,285):
            exit()
        elif x in xrange(418,466) and y in xrange(255,285):
            exitBoard.visible = 0
            end = 0
    #print mouseMove
    control.mouseCoord(*mouseMove)
    control.mouseDrag(*mouseMove)

@gameWindow.event

def on_draw():

    gameWindow.clear()
    mainBatch.draw()
    mapBatch.draw()
    loadobj.boxBatch.draw()
    boardBatch.draw()
    wordBatch.draw()
    buttomBatch.draw()
    fps_display.draw()
    blockBatch.draw()
    frame.numberBatch.draw()
    exitBatch.draw()
   # boom.draw()


def update(dt):
    victory = False
    GameOver = False




if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()
