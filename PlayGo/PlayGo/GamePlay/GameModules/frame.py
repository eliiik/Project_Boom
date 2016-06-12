# -*- coding:utf-8 -*-

import pyglet
import resource
import gamemap

LEFTSTEPS1 = 10
LEFTSTEPS2 = 30

numberBatch = pyglet.graphics.Batch()

class Scoreboard(pyglet.text.Label):
    def __init__(self, text, textX, textY, batch = None, *args, **kwargs):
        super(Scoreboard, self).__init__(text, x=textX, y=textY,  batch = batch, anchor_x='center',
                                         font_name = "Sans serif", font_size = 12, bold = True)

class Frame(pyglet.sprite.Sprite):
    def __init__(self, img, width, height, batch = None, *args, **kwargs):
        super(Frame, self).__init__(img, x = width, y = height, batch = batch)
  
class FrameNumber(Frame):
    def __init__(self, number, img, x, y, batch = None):
        super(FrameNumber, self).__init__(img, x, y, batch)
        self.number = number
#class StepBoard(pyglet.sprite.Sprite):
#    def __init__(self, img, width, height, batch = None, *args, **kwargs):
#        super(Frame, self).__init__(img, x = width, y = height, batch = batch)      
#        self.stepLeft = 20



#def setStepNumber(stepNumber, batch):
#    a = (stepNumber-stepNumber%10)/10
#    b = stepNumber % 10
#    print numberDict
#    print a,b
#    aStep = Frame(numberDict[2], 1,0, batch)
#    bStep = Frame(numberDict[3], 200,300, batch)
#    return aStep, bStep

class StepNumber(object):
    def __init__(self, stepNumber, batch = None, *args, **kwargs):
        self.numberDict = dict(zip(xrange(10),resource.numberList))
        self.frameNumberList = []
        self.numbers = self.setStepNumber(stepNumber)
        self.aNumer = FrameNumber(self.numbers[0], self.numberDict[self.numbers[0]],155,281, batch)
        self.frameNumberList.append(self.aNumer)
        self.bNumer = FrameNumber(self.numbers[1], self.numberDict[self.numbers[1]],194,281, batch)
        self.frameNumberList.append(self.bNumer)

    def __sub__(self, other):
        if gamemap.start:
            if self.bNumer.number == 0:
                if self.aNumer.number == 0:
                    return -1
                else:
                    self.aNumer.number -= other
                    self.aNumer.image = self.numberDict[self.aNumer.number]
                    self.bNumer.number = 9
                    self.bNumer.image = self.numberDict[self.bNumer.number]
            elif self.bNumer >= 0:
                self.bNumer.number -= other
                self.bNumer.image = self.numberDict[self.bNumer.number]

    def setStepNumber(self, stepNumber):
        a = (stepNumber-stepNumber%10)/10
        b = stepNumber % 10
        print a,b
        return a, b

class GameScore(Scoreboard):
    def __init__(self, text, textX, textY):
        super(GameScore, self).__init__(text, textX, textY, batch = numberBatch)
        self.font_size = 15

    def __add__(self, other):
        if gamemap.start:
            self.text = str(int(self.text)+other)


stepNumberList = StepNumber(LEFTSTEPS1, numberBatch)
gameScore = GameScore(text = '0', textX = 128, textY = 425)
goalScore = GameScore(text = str(gamemap.GOALS[gamemap.Level -1]), textX = 195, textY = 425)
