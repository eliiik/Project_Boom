# -*- coding:utf-8 -*-

import pyglet
import resource, box

def boxes(batch = None):
    boxes = []
    box_Xrange = [x for x in range(75,526,50)]
    box_Yrange = [y for y in range(85,536,50)]
    for i in xrange(10):
        newBox = box.Box(x = box_Xrange[i], y = box_Yrange[i], batch = batch)
        boxes.append(newBox)
    return boxes
