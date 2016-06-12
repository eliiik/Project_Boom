# -*- coding:utf-8 -*-
import pyglet

#定义常量
MARGINLOW = 66
MARGINHIGH = 66
MARGINLEFT = 299
BORDER = 4
BOARDSIZE = 468

NUMBERSIZE = 69

GOAL1 = 20
GOAL2 = 100
GOALS = [GOAL1, GOAL2]
#初始化游戏状态
start = 0
pause = 1
end = 0

#关卡
Level = 1
nextLevel = 0


# 0 -> empty, 1 -> box, 2 -> blocked
MAPARRAY1 = [[2,2,2,2,0,2,2,2,2],
             [2,2,2,0,0,0,2,2,2],
             [2,2,0,0,0,0,0,2,2],
             [2,0,0,0,0,0,0,0,2],
             [0,0,0,0,0,0,0,0,0],
             [2,0,0,0,0,0,0,0,2],
             [2,2,0,0,0,0,0,2,2],
             [2,2,2,0,0,0,2,2,2],
             [2,2,2,2,0,2,2,2,2]]
OBJIN1 = [(8,4)] #方块进入的坐标

MAPARRAY2 = [[2,2,2,2,2,0,0,2,2],
             [2,2,2,0,0,0,0,2,2],
             [0,0,0,0,0,0,0,2,2],
             [0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0],
             [2,2,0,0,0,0,0,0,0],
             [2,2,0,0,0,0,2,2,2],
             [2,2,0,0,2,2,2,2,2]]
OBJIN2 = [(8,5),(8,6)]

MAPARRAY = [MAPARRAY1, MAPARRAY2]
OBJIN = [OBJIN1, OBJIN2]

BOXIDARRAY = list((i,j) for i in range(9) for j in range(9))
#REMOVEPOINTS = [(0,0), (0,1), (1,0), (0,8), (0,9), (5,8), (5,9)]
#for i in REMOVEPOINTS:
#    BOXIDARRAY.remove(i)

#B  OXIDITERATOR = iter(BOXIDARRAY)