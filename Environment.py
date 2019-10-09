import turtle
from turtle import *
import numpy as np
import Rectangle
from Rectangle import *

SCREEN_X = 1000
SCREEN_Y = 1000
RECT_COLOR = 'blue'

turtle.screensize(SCREEN_X, SCREEN_Y)
turtle.ht()

r = Rectangle(0, 0, 50, 50, RECT_COLOR)
r.draw_rect()


turtle.done()
