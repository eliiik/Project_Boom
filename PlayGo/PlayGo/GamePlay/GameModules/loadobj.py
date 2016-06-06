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
        self.boxIDList = []
        self.allBoxes = []
        self.boxArray = list(reversed(MAPARRAY))
        self.boxCounter = {}
        # Generate box coord
        for i in xrange(10):
            for j in xrange(10):
                if self.boxArray[i][j] == 2:
                    self.boxesList[i].append(None)
                elif self.boxArray[i][j] != 2:
                    randint = random.randint(0,3)
                    boxCoord = self.getBoxCoord(j+1, i+1)
                    newBox = Box(resource.boxList[randint], x = boxCoord[0], y = boxCoord[1], batch = batch)
                    newBox.boxID = (i,j)
                    self.boxIDList.append(newBox.boxID)
                    #boxCoordList[i].append(boxCoord)
                    self.boxesList[i].append(newBox)
                    self.allBoxes.append(newBox)


    def __getitem__(self, index):
        return self.boxesList[index[0]][index[1]]

    def __setitem__(self, index, value):
        self.boxesList[index[0]][index[1]] = value


    def getBoxCoord(self, x, y):
        return ((x-0.5)*Box.BOXSIZE + BORDER + (x-1) * PADDING + MARGINLEFT,
                (y-0.5)*Box.BOXSIZE + BORDER + (y-1) * PADDING + MARGINLOW)

    #递归版本
    def threeMoreDeath(self, n, i = 1):
        try:
            if n >= 9:
                print 'shit', self[0,n].counterX, n, i
                return -1 
            elif id(self[0,n].image) != id(self[0, n+1].image):
                print self[0,n].counterX, n, i
                return n
            elif id(self[0,n].image) == id(self[0, n+1].image):
                self[0,n+1].counterX += i
                return self.threeMoreDeath(n+1, i+1)
        except(AttributeError):
            print "error", n, i
            return n

    def initBoxCounter(self):
        for i in self.allBoxes:
            i.counterX = i.counterY = 1

    def appendDict(self, word, dict):
        for w in word:
            if dict.has_key(w):
                dict[w] += 1
            else:
                dict[w] = 1


            
    #def checkNeighbor(self, boxID):
    #    crossX = [(0,x) for x in [-1,1]]
    #    crossY = [(y,0) for y in [-1,1]]


    #    for i in crossX:
    #        if self[(boxID[0] + i[0], boxID[1] + i[1])] == None:
    #            pass

    #        else:
    #            try:
    #                if id(self[boxID].image) == id(self[(boxID[0] + i[0], boxID[1] + i[1])].image):
    #                    self[boxID].counterX += 1
    #            except(IndexError, AttributeError):
    #                pass
    #    for j in crossY:
    #        if self[(boxID[0] + j[0], boxID[1] + j[1])] == None:
    #            pass
    #        else:
    #            try:
    #                if id(self[boxID].image) == id(self[(boxID[0] + i[0], boxID[1] + i[1])].image):
    #                    self[boxID].counterY += 1
    #            except(IndexError, AttributeError):
    #                pass
    #def threeMoreDeath(self):

    #    for i in BOXIDARRAY:
    #        self.checkNeighbor(i)
    #    try:
    #        for i in BOXIDARRAY:
    #            if self[i] == None:
    #                pass
    #            elif self[i].counterX > 3:
    #                self[i].delete()
    #            elif self[i].counterY > 3:
    #                self[i].delete()
    #    except(IndexError, AttributeError):
    #        pass




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



#def initNeighbor():
#    for i in
