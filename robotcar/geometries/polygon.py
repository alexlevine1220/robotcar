from robotcar.core import Geometry
from cv2 import cv2
import random
import numpy as np


class Polygon(Geometry):
    def __init__(self, color, rand, sideLength=None):
        """

        Arguments:
            Geometry {[type]} -- [description]
            vertices {[type]} -- [description]
        """
        if random == True:
            self.sideLength = sideLength
            self.color = color
        else:
            self.color = color

    def draw(self, map):
        return cv2.fillPoly(map, [np.array(self.vertices)], self.color)


class Rectangle(Polygon):
    def __init__(self, color, rand, vertices=None, sideLength=None, xInterval=None, yInterval=None):
        if rand == True and vertices == None:
            super().__init__(color, rand, sideLength)
            self.x1 = random.randint(xInterval[0], xInterval[1])
            self.y1 = random.randint(yInterval[0], yInterval[1])
            self.x2 = self.x1 + sideLength
            self.y2 = self.y1 + sideLength

            self.width = sideLength
            self.height = sideLength
        else:
            super().__init__(color, rand)

            if len(vertices) != 4:
                raise NotImplementedError

            self.x1 = vertices[0]
            self.y1 = vertices[1]
            self.x2 = vertices[2]
            self.y2 = vertices[3]
            self.width = abs(self.x2 - self.x1)
            self.height = abs(self.y2 - self.y1)

        self.center = ((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, 0)
        self.vertices = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y1), (self.x2, self.y2)]

    def containsPoint(self, x, y):
        return min(self.x1, self.x2) < x < max(self.x1, self.x2) and min(self.y1, self.y2) < y < max(self.y1, self.y2)
