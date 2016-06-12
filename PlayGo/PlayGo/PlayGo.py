#!/usr/bin/python
# -*- coding:utf-8 -*-

import pyglet
from pyglet.window import mouse, key
from GamePlay.GameModules import frame, resource, gamebox, loadobj, fx, gamemap
from GamePlay import control


mouseMove = [0,0,0,0]
gameWindow = pyglet.window.Window(800, 600)
gameWindow.set_icon(resource.icon1, resource.icon2)


mainBatch = pyglet.graphics.Batch()
mapBatch = pyglet.graphics.Batch()

boardBatch = pyglet.graphics.Batch()
wordBatch = pyglet.graphics.Batch()
buttomBatch = pyglet.graphics.Batch()
blockBatch = pyglet.graphics.Batch()
gameoverBatch = pyglet.graphics.Batch()
exitBatch = pyglet.graphics.Batch()

map1 = frame.Frame(resource.map1,533, 300,batch = mapBatch)
map1Block = frame.Frame(resource.map1,533, 300,batch = blockBatch)

map2 = frame.Frame(resource.map2,533, 300,batch = mapBatch)
map2Block = frame.Frame(resource.map2,533, 300,batch = blockBatch)
map2.visible = map2Block.visible = 0

bg = frame.Frame(resource.bg,400, 300, batch = mainBatch)
score = frame.Scoreboard("Score: ",128,450, wordBatch)
goal = frame.Scoreboard("Goal: ",200,450, wordBatch)
scoreBoard = frame.Frame(resource.scoreboard, 0, 391, boardBatch)
stepBoard = frame.Frame(resource.stepBoard,174,275,boardBatch)


pauseButton = frame.Frame(resource.pauseButton, 129,112, batch = buttomBatch)
pauseButton.visible = 0
startButton = frame.Frame(resource.startButton, 129,112, batch = buttomBatch)
exitButton = frame.Frame(resource.exitButton, 221,112, batch = buttomBatch)
exitBoard = frame.Frame(resource.exitBoard,400,300, batch = exitBatch)
exitBoard.visible = 0
nextLevel = frame.Frame(resource.nextLevel, 400,300, exitBatch)
nextLevel.visible = 0
gameover = frame.Frame(resource.gameover, 400,300, gameoverBatch)
gameover.visible = 0
#aStep = frame.Frame(frame.numberDict[2], 1,0, batch = frame.numberBatch)
#bStep = frame.Frame(frame.numberDict[3], 200,300, batch = frame.numberBatch)
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
    global exitBoard, map1Block, map2Block
    mouseMove[1] = x
    mouseMove[3] = y
    if x in xrange(107, 151) and y in xrange(90, 134):
        if gamemap.start:
            gamemap.pause = 1
            gamemap.start = 0
            startButton.visible = 1
            pauseButton.visible = 0
            map1Block.visible = 1
        else:
            gamemap.start = 1
            gamemap.pause = 0
            startButton.visible = 0
            pauseButton.visible = 1
            map1Block.visible = 0

    if x in xrange(199,243) and y in xrange(90,134):
        exitBoard.visible = 1
        gamemap.end = 1

    if gamemap.nextLevel == 1:
        if x in xrange(320,368) and y in xrange(255,285):
            nextLevel.visible = 0
            map2Block.visible = 0
            gamemap.nextLevel = 0
        elif x in xrange(418,466) and y in xrange(255,285):
            nextLevel.visible = 0
            gamemap.nextLevel = 0
            exit()

    if gamemap.end == 1:
        if x in xrange(320,368) and y in xrange(255,285):
            exit()
        elif x in xrange(418,466) and y in xrange(255,285):
            exitBoard.visible = 0
            end = 0


    control.mouseCoord(*mouseMove)
    control.mouseDrag(*mouseMove)

    if (control.checkLevel()):
        map1.visible = 0
        map2.visible = 1
        map2Block.visible = 1
        control.gameScore.text = "0"
        frame.goalScore.__init__(text = str(gamemap.GOALS[gamemap.Level -1]), textX = 195, textY = 425)
        try:
            loadobj.boxes.__del__()
        finally:
            nextLevel.visible = 1
            gamemap.nextLevel = 1
            loadobj.boxes.__init__(loadobj.boxBatch)
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
    gameoverBatch.draw()
    exitBatch.draw()
   # boom.draw()


def update(dt):
    victory = 0
    GameOver = 0

    if frame.stepNumberList.aNumer.number == frame.stepNumberList.bNumer.number == 0 and int(frame.gameScore.text) < int(frame.goalScore.text):
        GameOver = 1
        gameover.visible = 1
        if map1.visible == 1:
            map1Block.visible = 1
        elif map2.visible == 1:
            map2Block.visible = 1





if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()
