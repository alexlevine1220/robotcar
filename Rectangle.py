import turtle
from turtle import *
import numpy as np

class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.color = color
        self.topLeftX = x - (width / 2)
        self.bottomLeftX = self.topLeftX
        self.topRightX = x + (width / 2)
        self.bottomRightX = self.topRightX

        self.topLeftY = y + (height / 2)
        self.bottomLeftY = y - (height / 2)
        self.topRightY = self.topLeftY
        self.bottomRightY = self.bottomLeftY

    def draw_rect(self):
        turtle.speed(0)
        turtle.ht()
        turtle.color(self.color)
        turtle.fillcolor(self.color)

        turtle.begin_fill()

        turtle.up()
        turtle.goto(self.topLeftX, self.topLeftY)
        turtle.down()
        turtle.goto(self.topRightX, self.topRightY)
        turtle.goto(self.bottomRightX, self.bottomRightY)
        turtle.goto(self.bottomLeftX, self.bottomLeftY)
        turtle.goto(self.topLeftX, self.topLeftY)

        turtle.end_fill()
        turtle.done()
