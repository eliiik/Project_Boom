# -*- coding:utf-8 -*-
import pyglet
from gamebox import Box

#定义常量
MARGINLOW = 50
MARGINHIGH = 50
MARGINLEFT = 80
BORDER = 20
BOARDSIZE = 500
PADDING = (BOARDSIZE - Box.BOXAMOUNT*Box.BOXSIZE -2*BORDER)/(Box.BOXAMOUNT -1.0)
# 0 -> empty, 1 -> box, 2 -> blocked
MAPARRAY = [[0,0,0,0,0,2,0,0,0,0],
            [0,0,0,0,0,2,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0,0,0,2],
            [2,2,0,0,0,0,0,0,2,2]]

BOXIDARRAY = list((i,j) for i in range(10) for j in range(10))
REMOVEPOINTS = [(0,0), (0,1), (1,0), (0,8), (0,9), (5,8), (5,9)]
for i in REMOVEPOINTS:
    BOXIDARRAY.remove(i)

BOXIDITERATOR = iter(BOXIDARRAY)