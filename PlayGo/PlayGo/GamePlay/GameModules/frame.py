# -*- coding:utf-8 -*-

import pyglet




class Scoreboard(pyglet.text.Label):
    def __init__(self, text, textX, textY, batch = None, *args, **kwargs):
        super(Scoreboard, self).__init__(text, x=textX, y=textY,  batch = batch, anchor_x='center',
                                         font_name = "Sans serif", font_size = 16, bold = True)

class Frame(pyglet.sprite.Sprite):
    def __init__(self, img, width, height, batch = None, *args, **kwargs):
        super(Frame, self).__init__(img, x = width, y = height, batch = batch)
        
