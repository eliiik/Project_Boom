# -*- coding:utf-8 -*-

import pyglet
import resource, random, gamemap
from gamebox import Box
from gamemap import *


#boxCoordList = [[] for i in range(10)]
boxBatch = pyglet.graphics.Batch()

class Boxgenerate(Box):
    def __init__(self,batch = None, *args, **kwargs):
        self.boxesList = [[] for i in range(10)]
        self.boxArray = list(reversed(MAPARRAY))
        # Generate box coord
        for i in xrange(10):
            for j in xrange(10):
                if self.boxArray[i][j] == 2:
                    self.boxesList[i].append(None)
                elif self.boxArray[i][j] != 2:
                    randint = random.randint(0,3)
                    boxCoord = self.getBoxCoord(j+1, i+1)
                    newBox = Box(resource.boxList[randint], x = boxCoord[0], y = boxCoord[1], batch = batch)
                    #boxCoordList[i].append(boxCoord)
                    self.boxesList[i].append(newBox)

    def __getitem__(self, index):
        return self.boxesList[index[0]][index[1]]

    def __setitem__(self, index, value):
        self.boxesList[index[0]][index[1]] = value


    def getBoxCoord(self, x, y):
        return ((x-0.5)*Box.BOXSIZE + BORDER + (x-1) * PADDING + MARGINLEFT,
                (y-0.5)*Box.BOXSIZE + BORDER + (y-1) * PADDING + MARGINLOW)

boxes = Boxgenerate(batch = boxBatch)

def swap(a, b):
    try:
        if boxes.boxArray[b[0]][b[1]] == 2:
            pass
        else:
            boxes[a], boxes[b] = boxes[b], boxes[a]
            boxes[a].x, boxes[b].x = boxes[b].x, boxes[a].x
            boxes[a].y, boxes[b].y = boxes[b].y, boxes[a].y
    except(AttributeError):
        pass

def checkNeighbor(boxID):
    crossX = [(x,0) for x in [-1,1]]
    crossY = [(0,y) for y in [-1,1]]

    try:
        for i in crossX:
            if id(boxes[boxID].image) == id(boxes[(boxID[0] + i[0], boxID[1] + i[1])].image):
                boxes[boxID].counterX += 1
        for j in crossY:
            if id(boxes[boxID].image) == id(boxes[(boxID[0] + j[0], boxID[1] + j[1])].image):
                boxes[boxID].counterY += 1
    except(IndexError, AttributeError):
        pass

#def initNeighbor():
#    for i in
