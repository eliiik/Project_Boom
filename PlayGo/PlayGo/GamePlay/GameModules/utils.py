# -*- coding:utf-8 -*-

import pyglet

def centerImage(*image):
    #中置图片坐标轴
    for i in range(len(image)):
        image[i].anchor_x = image[i].width//2
        image[i].anchor_y = image[i].height//2