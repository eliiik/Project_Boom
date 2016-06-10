# -*- coding:utf-8 -*-

import pyglet
import resource, random, gamemap
from gamebox import Box
from gamemap import *


#boxCoordList = [[] for i in range(9)]
boxBatch = pyglet.graphics.Batch()

class Boxgenerate():
    def __init__(self,batch = None, *args, **kwargs):
        self.boxesList = [[] for i in range(9)]
        self.boxIDList = []
        self.allBoxes = []
        self.boxArray = list(reversed(MAPARRAY1))
        self.boxCounter = {}
        # Generate box coord
        for i in xrange(9):
            for j in xrange(9):
                if self.boxArray[i][j] == 2:
                    self.boxesList[i].append(None)
                elif self.boxArray[i][j] != 2:
                    self.randint = random.randint(0,3)
                    newBox = self.createBox(self.randint, (i,j), batch)
                    self.boxIDList.append(newBox.boxID)
                    #boxCoordList[i].append(boxCoord)
                    self.boxesList[i].append(newBox)
                    self.allBoxes.append(newBox)


    def __getitem__(self, index):
        return self.boxesList[index[0]][index[1]]

    def __setitem__(self, index, value):
        self.boxesList[index[0]][index[1]] = value

    #def __iter__(self):
    #    return self.boxesList

    #def __next__(self):

    def createBox(self,randint, boxID, batch):
        self.boxArray[boxID[0]][boxID[1]] = 1
        return Box(resource.boxList[randint], boxID, batch = batch)
    #递归版本
    def threeMoreDeath(self, m, n, i = 1):
        if n >= 8:
            print 'shit', self[m,n].counterX, n, i
            if self[m,n].counterX >= 3:
                for killbox in self.boxesList[m][n-i+1:n+1]:
                    self.delete(killbox)
            return -1 

        elif id(self[m,n].image) != id(self[m, n+1].image):
            print "oh", self[m,n].counterX, n, i
            if self[m,n].counterX >= 3:
                for killbox in self.boxesList[m][n-i+1:n+1]:
                    self.delete(killbox)
                print type(self[m,n])
            return self.threeMoreDeath(m, n+1, i = 1)

        elif id(self[m,n].image) == id(self[m, n+1].image):
            self[m,n+1].counterX += i
            return self.threeMoreDeath(m, n+1, i+1)

    def delete(self, boxName):
        print "delete1"
        boxName.deleteBox()
        #self[boxName.boxID[0], boxName.boxID[1]] = None
        self.boxArray[boxName.boxID[0]][boxName.boxID[1]] = 0

    def initBoxCounter(self):
        for i in self.allBoxes:
            i.initBoxCounter()

    def appendDict(self, word, dict):
        for w in word:
            if dict.has_key(w):
                dict[w] += 1
            else:
                dict[w] = 1
    #递归版
    def checkEmpty(self, boxID):
        try:
            if self.boxArray[boxID[0]][boxID[1]] == 0:
                return True
            else:
                return False
        except(TypeError, AttributeError):
            return False

    def moveDown(self, boxID):
        if self.checkEmpty(boxID):
            if self.checkUpwards(boxID) == 1:                
                self.moveDown(self.swapUpDown(boxID))
            elif self.checkUpwards(boxID) == 2:
                self.moveDown(self.swapLeftOrRight(boxID))
            elif self.checkUpwards(boxID) == 0:
                newID = self.swapUpDown(boxID)
                self[newID] = self.createBox(random.randint(0,3), newID, batch = boxBatch)
                self.boxArray[newID[0]][newID[1]] = 1
                print "Fucking out!"
                return 0
        else:
            return

    def moveAllDown(self):
        for i in self.boxIDList:
            self.moveDown(i)

    def checkUpwards(self, boxID):
        try:
            checker = self.boxArray[boxID[0]+1][boxID[1]]
            if checker == 2:
                return 2
            elif (boxID[0]+1, boxID[1]) == OBJIN1:
                return 0
            elif checker in (0, 1):
                return 1
        except(IndexError):
            return 0
    
    def swapLeftOrRight(self, boxID):
        if boxID[1] < OBJIN1[1]:
            #swapRight
            newID = [boxID[0], boxID[1]+1]
            self.swap(boxID, newID)
            return newID
        else:
            #swapLeft
            newID = [boxID[0], boxID[1]-1]
            self.swap(boxID, newID)
            return newID

    def swapUpDown(self, boxID):
        newID = [boxID[0]+1, boxID[1]]
        self.swap(boxID, newID)
        return newID

    def swap(self, a, b):
        self[a], self[b] = self[b], self[a]
        self[a].boxID, self[b].boxID = self[b].boxID, self[a].boxID
        self.boxArray[a[0]][a[1]], self.boxArray[b[0]][b[1]] = self.boxArray[b[0]][b[1]], self.boxArray[a[0]][a[1]]
        self[a].x, self[b].x = self[b].x, self[a].x
        self[a].y, self[b].y = self[b].y, self[a].y
    

boxes = Boxgenerate(batch = boxBatch)



    #except(AttributeError):
    #    pass





    
            
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




#def initNeighbor():
#    for i in
