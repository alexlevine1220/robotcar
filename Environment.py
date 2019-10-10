import turtle
from turtle import *
import numpy as np
import Rectangle
from Rectangle import *

# Cosntants
SCREEN_X = 1000
SCREEN_Y = 1000
RECT_COLOR = 'blue'

def main():
    turtle.screensize(SCREEN_X, SCREEN_Y)
    turtle.ht()

    turtle.listen() # listen for mouse events
    turtle.onscreenclick(clickDraw)

    turtle.mainloop()



def clickDraw(x, y):
    print("New Rectangle at: " + str(x) + " " + str(y))
    r = Rectangle(y, x, 50, 50, RECT_COLOR)
    r.draw_rect()


main()
turtle.done()
