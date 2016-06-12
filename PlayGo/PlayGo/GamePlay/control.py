# -*- coding:utf-8 -*-

import pyglet
from pyglet.window import mouse
from GameModules.gamebox import Box
from GameModules.gamemap import *
from GameModules.loadobj import boxes
from GameModules.frame import *
import math
numberBatch = pyglet.graphics.Batch()
initCoord = [-1,-1]
#保存初始坐标
def mouseCoord(*args):
    px = args[0]
    py = args[2]

    initCoord[0] = px
    initCoord[1] = py

#获取鼠标拖动方向
def mouseDrag(*args):
    global LEFTSTEPS1, LEFTSTEPS2
    dx = args[1] - args[0]
    dy = args[3] - args[2]

    def sin(x, y):
        try:
            return(y / math.sqrt(x**2 + y**2))
        except(ZeroDivisionError):
            pass

    sinM = sin(dx, dy)

    if sinM == None:
        dragCoord = -1
    elif sinM > 1/math.sqrt(2):
        dragCoord = 2
    elif sinM < -1/math.sqrt(2):
        dragCoord = 4
    elif dx > 0:
        dragCoord = 1
    else:
        dragCoord = 3
    boxID = getBoxID(initCoord)

    dragBox(boxID,dragCoord)

    while 1:
        boxes.getKilled = 0
        boxes.moveAllDown()
        for i in xrange(9):
        #    print "getkilledinloop: ", boxes.getKilled
            boxes.threeMoreDeath(i,0)
            boxes.threeMoreDeathY(0,i)
        boxes.moveAllDown()
        boxes.initBoxCounter()
       # boxes.getKilled -= 1
       # print "getkilled: ", boxes.getKilled
        if boxes.getKilled != 1:
            break

def getBoxID(args):
    m = (args[1] - MARGINLOW - BORDER + 0.5 * Box.BOXSIZE + Box.PADDING) / (Box.BOXSIZE + Box.PADDING)
    n = (args[0] - MARGINLEFT - BORDER + 0.5 * Box.BOXSIZE + Box.PADDING) / (Box.BOXSIZE + Box.PADDING)
    print m
    print n
    print (int(round(m))-1,int(round(n))-1)
    return (int(round(m))-1,int(round(n))-1)

def dragBox(boxID, dragCoord):
    try:
        if boxID[0] < 0 or boxID[1] < 0:
            return
        if boxes.boxArray[boxID[0]][boxID[1]] != 2:
            if dragCoord == -1:
                return
            elif dragCoord == 1:
                stepNumberList - 1
                boxes.swap(boxID, (boxID[0], boxID[1] + 1))
            elif dragCoord == 2:
                stepNumberList - 1
                boxes.swap(boxID, (boxID[0] + 1, boxID[1]))
            elif dragCoord == 3:
                stepNumberList - 1
                boxes.swap(boxID, (boxID[0], boxID[1] - 1))
            elif dragCoord == 4:
                stepNumberList - 1
                boxes.swap(boxID, (boxID[0] - 1, boxID[1]))
    except(IndexError):
        return

def checkLevel():
    if int(gameScore.text) >= int(goalScore.text):
        gamemap.Level += 1
        return 1
    else:
        return 0