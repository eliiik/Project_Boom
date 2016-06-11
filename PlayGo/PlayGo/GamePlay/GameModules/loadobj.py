# -*- coding:utf-8 -*-

import pyglet
import resource, random, gamemap
from gamebox import Box
from gamemap import *
import math
from pyglet.app.base import EventLoop

#boxCoordList = [[] for i in range(9)]
boxBatch = pyglet.graphics.Batch()

class Boxgenerate(object):
    def __init__(self,batch = None, *args, **kwargs):
        self.boxesList = [[] for i in range(9)]
        self.boxIDList = []
        self.allBoxes = []
        self.boxArray = list(reversed(MAPARRAY1))
        self.boxCounter = {}
        self.getKilled = 0
        # Generate box coord
        for i in xrange(9):
            for j in xrange(9):
                if self.boxArray[i][j] == 2:
                    self.boxesList[i].append(None)
                elif self.boxArray[i][j] != 2:
                    self.randint = random.randint(0,4)
                    newBox = self.createBox(self.randint, (i,j), batch)
                    self.boxIDList.append(newBox.boxID)
                    self.boxesList[i].append(newBox)
                    self.allBoxes.append(newBox)
                    #boxCoordList[i].append(boxCoord)


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

        if self.boxArray[m][n] == 2:
            #print "myshit"
            return self.threeMoreDeath(m, n+1, i)

        elif n >= 8 or self.boxArray[m][n+1] == 2:
            #print 'shit', self[m,n].counterX, n, i
            if self[m,n].counterX >= 3:
                self.getKilled = 1
                for killbox in self.boxesList[m][n-i+1:n+1]:
                    self.delete(killbox)
            return -1

        elif id(self[m,n].image) != id(self[m, n+1].image):
            #print "oh", self[m,n].counterX, n, i
            if self[m,n].counterX >= 3:
                self.getKilled = 1
                for killbox in self.boxesList[m][n-i+1:n+1]:
                    self.delete(killbox)
            return self.threeMoreDeath(m, n+1, i = 1)

        elif id(self[m,n].image) == id(self[m, n+1].image):
            self[m,n+1].counterX += i
            return self.threeMoreDeath(m, n+1, i+1)

    def threeMoreDeathY(self, m, n, i = 1):

        if self.boxArray[m][n] == 2:
            #print "myshit"
            return self.threeMoreDeathY(m+1, n, i)

        elif m >= 8 or self.boxArray[m+1][n] == 2:
            #print 'shit', self[m,n].counterX, n, i
            if self[m,n].counterY >= 3:
                self.getKilled = 1
                for killbox in self.boxesList[m-i+1:m+1]:
                    self.delete(killbox[n])
            return -1

        elif id(self[m,n].image) != id(self[m+1, n].image):
            #print "oh", self[m,n].counterX, n, i
            if self[m,n].counterY >= 3:
                self.getKilled = 1
                for killbox in self.boxesList[m-i+1:m+1]:
                    self.delete(killbox[n])
            return self.threeMoreDeathY(m+1, n, i = 1)

        elif id(self[m,n].image) == id(self[m+1, n].image):
            self[m+1,n].counterY += i
            return self.threeMoreDeathY(m+1, n, i+1)


    def delete(self, boxName):
        #print "delete1"
        boxName.deleteBox()
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
            checkreturn = self.checkUpwards(boxID)
            if checkreturn == 1:                
                self.moveDown(self.swapUpDown(boxID))
            elif checkreturn == 2:
                self.moveDown(self.swapLeftOrRight(boxID))
            elif checkreturn == 3:
                newID = self.swapUpDown(boxID)
                self[newID].image = resource.boxList[random.randint(0,4)]
                self[newID].visible = True
                self[newID].scale = 1
                self.boxArray[newID[0]][newID[1]] = 1
                #print "Fucking out!"
                return
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
                return 3
            elif checker in (0, 1):
                return 1
        except(IndexError):
            return -1
    
    def swapLeftOrRight(self, boxID):
        if boxID[1] < OBJIN1[1]:
            #swapRight
            newID = [boxID[0], boxID[1]+1]
            self.swap(boxID, newID)
            #self.swapEventLoop.sleep(1)
            #swapObj = swapLoop(boxID, newID)
            #for i in range(60):
            #    swapObj.run()
            #pyglet.clock.schedule_interval(self.swap, 1/120.0, boxID, newID)
            #self.swapEventLoop.sleep(0.5)
            #pyglet.clock.unschedule(self.swap)

            return newID
        else:
            #swapLeft
            newID = [boxID[0], boxID[1]-1]
            self.swap(boxID, newID)
            #swapObj = swapLoop(boxID, newID)
            #for i in range(60):
            #    swapObj.run()
            #pyglet.clock.schedule_interval(self.swap, 1/120.0, boxID, newID)
            #self.swapEventLoop.sleep(0.5)
            #pyglet.clock.unschedule(self.swap)
            return newID

    def swapUpDown(self, boxID):
        newID = [boxID[0]+1, boxID[1]]
        self.swap(boxID, newID)
        #self.swapEventLoop.sleep(1)
        #swapObj = swapLoop(boxID, newID)
        #for i in range(60):
        #    swapObj.run()
        #pyglet.clock.schedule_interval(self.swap, 1/120.0, boxID, newID)
        #self.swapEventLoop.sleep(0.5)
        #pyglet.clock.unschedule(self.swap)        
        return newID

    def swap(self, a, b):
        if self[b]:
            self[a], self[b] = self[b], self[a]
            self[a].boxID, self[b].boxID = self[b].boxID, self[a].boxID
            self.boxArray[a[0]][a[1]], self.boxArray[b[0]][b[1]] = self.boxArray[b[0]][b[1]], self.boxArray[a[0]][a[1]]
            self[a].x, self[b].x = self[b].x, self[a].x
            self[a].y, self[b].y = self[b].y, self[a].y

#class swapLoop(Boxgenerate, EventLoop):
#    def __init__(self,a,b):
#        super(swapLoop, self).__init__()
#        self.a = a
#        self.b = b
#        self[a], self[b] = self[b], self[a]
#        self[a].boxID, self[b].boxID = self[b].boxID, self[a].boxID
#        self.boxArray[a[0]][a[1]], self.boxArray[b[0]][b[1]] = self.boxArray[b[0]][b[1]], self.boxArray[a[0]][a[1]]
#        #self[a].x, self[b].x = self[b].x, self[a].x
#        #self[a].y, self[b].y = self[b].y, self[a].y
#        dx = self[b].x - self[a].x
#        dy = self[b].y - self[a].y
#        self.dxt = dx / 60.0
#        self.dyt = dy / 60.0
#        self.animate()

#    def __getitem__(self, index):
#        return self.boxesList[index[0]][index[1]]

#    def __setitem__(self, index, value):
#        self.boxesList[index[0]][index[1]] = value

#    def animate(self):
#        self[self.a].x += self.dxt
#        self[self.b].x -= self.dxt
#        self[self.a].y += self.dyt
#        self[self.b].y -= self.dyt


'''class swapLoop(Boxgenerate, EventLoop):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self[a], self[b] = self[b], self[a]
        self[a].boxID, self[b].boxID = self[b].boxID, self[a].boxID
        self.boxArray[a[0]][a[1]], self.boxArray[b[0]][b[1]] = self.boxArray[b[0]][b[1]], self.boxArray[a[0]][a[1]]
        #self[a].x, self[b].x = self[b].x, self[a].x
        #self[a].y, self[b].y = self[b].y, self[a].y
        dx = self[b].x - self[a].x
        dy = self[b].y - self[a].y
        dxt = dx / 60.0
        dyt = dy / 60.0

    def animate(self):
        self[self.a].x += self.dxt
        self[self.b].x -= self.dxt
        self[self.a].y += self.dyt
        self[self.b].y -= self.dyt'''
    
    

'''
    def swap(self,dt , a, b):
        self[a], self[b] = self[b], self[a]
        self[a].boxID, self[b].boxID = self[b].boxID, self[a].boxID
        self.boxArray[a[0]][a[1]], self.boxArray[b[0]][b[1]] = self.boxArray[b[0]][b[1]], self.boxArray[a[0]][a[1]]
        #self[a].x, self[b].x = self[b].x, self[a].x
        #self[a].y, self[b].y = self[b].y, self[a].y
        dx = self[b].x - self[a].x
        dy = self[b].y - self[a].y
        dxt = dx / 60.0
        dyt = dy / 60.0
        self.calltimes = 0
        def animate(a,b,dxt,dyt):
            self[a].x += dxt
            self[b].x -= dxt
            self[a].y += dyt
            self[b].y -= dyt
            self.calltimes += 1
        #if self.calltimes == 0:
        #    pyglet.clock.schedule_interval(animate, 1/120.0, a,b,dxt,dyt)

'''

'''

    #swapEventLoop.exit_blocking()
    def swap(self,dt, a, b):
        self[a], self[b] = self[b], self[a]
        self[a].boxID, self[b].boxID = self[b].boxID, self[a].boxID
        self.boxArray[a[0]][a[1]], self.boxArray[b[0]][b[1]] = self.boxArray[b[0]][b[1]], self.boxArray[a[0]][a[1]]
        #self[a].x, self[b].x = self[b].x, self[a].x
        #self[a].y, self[b].y = self[b].y, self[a].y
        dx = self[b].x - self[a].x
        dy = self[b].y - self[a].y
        dxt = dx / 60.0
        dyt = dy / 60.0
        self.calltimes = 0
        self[a].x += dxt
        self[b].x -= dxt
        self[a].y += dyt
        self[b].y -= dyt
        self.calltimes += 1
        if self.calltimes == 0:
            pyglet.clock.schedule_interval(animate, 1/120.0, a,b,dxt,dyt)
        #while 1:
        #    if self.calltimes == 0:
        #        pyglet.clock.schedule_interval(animate, 1/120.0, a,b,dxt,dyt)
        #        #pyglet.clock.schedule_interval(animate(a,b,dxt,dyt), 1/120.0)
        #    #self.animate(a,b,dxt,dyt)
        #    elif self.calltimes >= 60:
        #        pyglet.clock.unschedule(animate, 0)
        #        break
    
    #def animate(self,a,b,dxt,dyt):
    #    pyglet.clock.schedule_interval(self.animate(a,b,dxt,dyt), 1/120.0)

    #    self[a].x += dxt
    #    self[b].x -= dxt
    #    self[a].y += dyt
    #    self[b].y -= dyt
    #    self.calltimes += 1

        #def quitAnimation(dt):
        #    pyglet.clock.unschedule(animate)
        #    return calltimes + 1
        #pyglet.clock.schedule_interval(animate, 1/120.0)
        #pyglet.clock.schedule_once(quitAnimation, 1)
        #pyglet.media.WorkerThread.sleep(1)
        #if self.calltimes >= 60:
        #    pyglet.clock.unschedule(animate)
        #    break

        #animate = pyglet.media.WorkerThread()
        #animate.get_job(
'''

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
