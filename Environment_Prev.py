import turtle
from turtle import *
import numpy as np
import Rectangle
from Rectangle import *
import random

# Cosntants
SCREEN_X = 1000
SCREEN_Y = 1000
RECT_COLOR = 'blue'
DIM_OFFSET = 30
WIDTH = 50
HEIGHT = 50
DIVISOR = 2

def main():
    turtle.screensize(SCREEN_X, SCREEN_Y)
    turtle.ht()

    totalRects = [] # Array that keeps track of the total amount of rectangles

    print("Enter the number rectangles between 1 and 10: ")
    numRects = input()
    valid = True
    while(valid):
        if(numRects.isdigit() == False):
            print("Error, user input was not a number.")
            print("Enter the number rectangles between 1 and 10: ")
            numRects = input()
        else:
            numRects = int(numRects)

            if (numRects < 1 or numRects > 10):
                print("Error, value entered is out of bounds.")
                print("Enter the number rectangles between 1 and 10: ")
                numRects = input()
            else:
                valid = False

    rect = 0
    for i in range(numRects):
        x = random.randint(0 - (SCREEN_X / DIVISOR) + WIDTH, (SCREEN_X / DIVISOR) - WIDTH)
        y = random.randint(0 - (SCREEN_Y / DIVISOR) + HEIGHT, (SCREEN_Y / DIVISOR) - HEIGHT)

        valid = True
        print(i)
        # for j in range(len(totalRects)):
        #     r = totalRects[j]
        #
        #     xLeft = x - (WIDTH / 2)
        #     xRight = x + (WIDTH / 2)
        #     yBottom = y - (HEIGHT / 2)
        #     yTop = y + (HEIGHT / 2)
        #
        #     rLeftOffsetX = r.topLeftX - DIM_OFFSET
        #     rRightOffsetX = r.topRightX + DIM_OFFSET
        #     rBottomOffsetY = r.bottomRightY - DIM_OFFSET
        #     rTopOffsetY = r.topRightY + DIM_OFFSET
        #
        #     if (xLeft >= rLeftOffsetX and xLeft <= rRightOffsetX and yTop >= rBottomOffsetY and yTop <= rTopOffsetY):
        #         valid = False
        #     elif(xLeft >= rLeftOffsetX and xLeft <= rRightOffsetX and yBottom >= rBottomOffsetY and yBottom <= rTopOffsetY):
        #         valid = False
        #     elif(xRight >= rLeftOffsetX and xRight <= rRightOffsetX and yTop >= rBottomOffsetY and yTop <= rTopOffsetY):
        #         valid = False
        #     elif(xRight >= rLeftOffsetX and xRight <= rRightOffsetX and yBottom >= rBottomOffsetY and yBottom <= rTopOffsetY):
        #         valid = False
        #
        # print("herre")
        # if (valid):
        #     rect = Rectangle(x, y, WIDTH, HEIGHT, RECT_COLOR)
        #     rect.draw_rect()
        #     totalRects.append(rect)
        # else:
        #     i = i - 1
        rect = Rectangle(x, y, WIDTH, HEIGHT, RECT_COLOR)
        rect.draw_rect()

    # turtle.listen() # listen for mouse events
    # turtle.onscreenclick(clickDraw)
    turtle.mainloop()

main()
turtle.done()



# def clickDraw(x, y):
#     global totalRects
#     invalidX = False
#     invalidY = False
#     width = 50
#     height = 50
#
#     xCMinus = x - (width / DIVISOR)
#     xCPlus = x + (width / DIVISOR)
#     yCMinus = y - (height / DIVISOR)
#     yCPlus = y + (height / DIVISOR)
#
#     for r in totalRects:
#         invalidX = False
#         invalidY = False
#
#         rLeftOffsetX = r.topLeftX - DIM_OFFSET
#         rRightOffsetX = r.topRightX + DIMOFFSET
#         rBottomOffsetY = r.bottomRightY - DIM_OFFSET
#         rTopOffsetY = r.topRightY + DIM_OFFSET
#
#         if((xCPlus >= rLeftOffsetX and xCPlus <= rRightOffsetX) or (xCMinus >= rLeftOffsetX and xCMinus <= rRightOffsetX)):
#             invalidX = True
#
#         if((yCPlus >= rLeftOffsetY and yCPlus <= rRightOffsetY) or (yCMinus >= rLeftOffsetY and yCMinus <= rRightOffsetY)):
#             invalidY = True
#
#     if (invalidX or invalidY):
#         print("\nInvalid position, rectangle overlap")
#     else:
#         print("\nNew Rectangle at: " + str(x) + " " + str(y))
#         rect = Rectangle(x, y, width, height, RECT_COLOR)
#         rect.draw_rect()
#         totalRects.append(rect)
#         print(totalRects)
