# -*- coding:utf-8 -*-

import pyglet
import resource

LEFTSTEPS1 = 40
LEFTSTEPS2 = 30

numberBatch = pyglet.graphics.Batch()

class Scoreboard(pyglet.text.Label):
    def __init__(self, text, textX, textY, batch = None, *args, **kwargs):
        super(Scoreboard, self).__init__(text, x=textX, y=textY,  batch = batch, anchor_x='center',
                                         font_name = "Sans serif", font_size = 12, bold = True)

class Frame(pyglet.sprite.Sprite):
    def __init__(self, img, width, height, batch = None, *args, **kwargs):
        super(Frame, self).__init__(img, x = width, y = height, batch = batch)
  
#class StepBoard(pyglet.sprite.Sprite):
#    def __init__(self, img, width, height, batch = None, *args, **kwargs):
#        super(Frame, self).__init__(img, x = width, y = height, batch = batch)      
#        self.stepLeft = 20

numberDict = dict(zip(xrange(10),resource.numberList))

def setStepNumber(stepNumber):
    a = (stepNumber-stepNumber%10)/10
    b = stepNumber % 10
    print numberDict
    print a,b



