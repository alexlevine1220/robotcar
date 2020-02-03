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
