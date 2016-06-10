# -*- coding:utf-8 -*-

import pyglet
import fx
from pyglet.window import mouse
from gamemap import *

class Box(pyglet.sprite.Sprite):
    BOXSIZE = 50
    BOXAMOUNT = 9
    PADDING = (BOARDSIZE - BOXAMOUNT*BOXSIZE -2*BORDER)/(BOXAMOUNT -1.0)

    def __init__(self, initbox, boxID, *args, **kwargs):
        super(Box, self).__init__(initbox, *args, **kwargs)
        
        #super(Box, self).height = self.BOXSIZE
        #super(Box, self).width = self.BOXSIZE
        self.updateCoord(boxID)
        self.counterX = 1
        self.counterY = 1
        self.boxID = [boxID[0], boxID[1]]
        #self.mouseHandler = control.on_mouse_drag()
    def getBoxCoord(self, x, y):
        return ((x-0.5)*self.BOXSIZE + BORDER + (x-1) * self.PADDING + MARGINLEFT,
                (y-0.5)*self.BOXSIZE + BORDER + (y-1) * self.PADDING + MARGINLOW)

    def IDtoCoord(self, boxID):
        return self.getBoxCoord(boxID[1]+1, boxID[0]+1)

    def move(x):
        pass

    def updateCoord(self, newID):
        #super(Box, self).update(dt)
        newCoord = self.IDtoCoord(newID)
        self.x = newCoord[0]
        self.y = newCoord[1]
        pass

    def deleteBox(self):
        print 'delete 2'
        self.visible = False

    def boom(self):

        pass
    def boomAnimation(self):
        pass

    def initBoxCounter(self):
        self.counterX = self.counterY = 1






    #def boomAnimation(self):
    #    self.explosion = pyglet.image.load('Explosion.png')
    #    self.explosion_seq = pyglet.image.ImageGrid(explosion, 1, 8)
    #    self.animation = pyglet.image.load_animation(self.explosion_seq)
    #    self.bin = pyglet.image.atlas.TextureBin()
    #    self.animation.add_to_texture_bin(self.bin)
    #    self.sprite = pyglet.sprite.Sprite(self.animation)


    
