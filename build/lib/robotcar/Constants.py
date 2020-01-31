from enum import Enum


class Color:
    ROBOT = (255, 0, 0)
    OBSTACLE = (0, 0, 0)
    GOAL = (0, 0, 255)
    BLANK = (255, 255, 255)


class Robot_Types:
    CIRCLE = "CIRCLE"
    RECTANGLE = "RECTANGLE"
