# -*- coding:utf-8 -*-

import pyglet
import fx
from pyglet.window import mouse

class Box(pyglet.sprite.Sprite):
    BOXSIZE = 30
    BOXAMOUNT = 10

    def __init__(self, initbox, *args, **kwargs):
        super(Box, self).__init__(initbox, *args, **kwargs)
        
        #super(Box, self).height = self.BOXSIZE
        #super(Box, self).width = self.BOXSIZE
        self.counterX = 1
        self.counterY = 1
        #self.mouseHandler = control.on_mouse_drag()

    def move(x):
        pass

    def update(self, dt):
        #super(Box, self).update(dt)
        pass

    def delete(self):
        if self:
            return super(Box, self).delete()

    def boom(self):

        pass
    def boomAnimation(self):
        pass
    #def boomAnimation(self):
    #    self.explosion = pyglet.image.load('Explosion.png')
    #    self.explosion_seq = pyglet.image.ImageGrid(explosion, 1, 8)
    #    self.animation = pyglet.image.load_animation(self.explosion_seq)
    #    self.bin = pyglet.image.atlas.TextureBin()
    #    self.animation.add_to_texture_bin(self.bin)
    #    self.sprite = pyglet.sprite.Sprite(self.animation)


    
