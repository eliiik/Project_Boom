# -*- coding:utf-8 -*-

import pyglet
import resource

def boxBoom():
   # explosion = pyglet.image.load()
    explosion_seq = pyglet.image.ImageGrid(resource.boom, 1, 8)
    explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
    #animation = pyglet.image.load_animation(explosion_seq)
    #bin = pyglet.image.atlas.TextureBin()
    #animation.add_to_texture_bin(bin)
    boom = [pyglet.sprite.Sprite(explosion_tex_seq[i], x = 400, y = 300) for i in range(1,8)]
    return boom

def update(dt):
    for i in boom:
        i.visible = True
