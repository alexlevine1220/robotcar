import vtkplotter


def create_geometry(config):
    if config["type"] == "RECTANGLE":
        return Rectangle(config["x"], config["y"], config["width"], config["height"])


class Geometry:
    def __init__(self):
        raise NotImplementedError

    def vtk_object(self, color):
        raise NotImplementedError


class Rectangle(Geometry):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vertices = [(x - width / 2, y - height / 2), (x - width / 2)]

    def vtk_object(self, color):
        return vtkplotter.Box((self.x, self.y, 0), self.width, self.height, 5, size=(), c=color)


class Line(Geometry):
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def vtk_object(self, color):
        return vtkplotter.Line((self.x1, self.y1), (self.x2, self.y2), c=color)
