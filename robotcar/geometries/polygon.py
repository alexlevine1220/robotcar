from robotcar.core import Geometry
from cv2 import cv2
import numpy as np


class Polygon(Geometry):
    def __init__(self, vertices, color):
        """

        Arguments:
            Geometry {[type]} -- [description]
            vertices {[type]} -- [description]
        """
        self.vertices = vertices
        self.color = color

    def draw(self, map):
        return cv2.fillPoly(map, [np.array(self.vertices)], self.color)


class Rectangle(Polygon):
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)
        self.center = ((x1 + x2) / 2, (y1 + y2) / 2, 0)

    def containsPoint(self, x, y):
        return min(self.x1, self.x2) < x < max(self.x1, self.x2) and min(self.y1, self.y2) < y < max(self.y1, self.y2)
