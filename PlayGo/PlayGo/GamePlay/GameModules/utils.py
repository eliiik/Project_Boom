# -*- coding:utf-8 -*-

import pyglet

def centerImage(*image):
    #中置图片坐标轴
    for i in image:
        i.anchor_x = i.width//2
        i.anchor_y = i.height//2