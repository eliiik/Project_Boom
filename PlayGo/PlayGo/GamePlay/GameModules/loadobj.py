# -*- coding:utf-8 -*-

import pyglet
import resource, box, random

def boxes(batch = None):
    boxes = []
    box_Xrange = [x for x in range(75,526,50)]
    box_Yrange = [y for y in range(85,536,50)]
    for i in xrange(10):
        for j in xrange(10):
            randint = random.randint(0,3)
            newBox = box.Box(resource.boxTuple[randint], x = box_Xrange[i], y = box_Yrange[j], batch = batch)
            boxes.append(newBox)
    return boxes

