def create_geometry(config):
    if config["type"] == "RECTANGLE":
        return Rectangle(config["x"], config["y"], config["width"], config["height"])


class Geometry:
    def __init__(self):
        raise NotImplementedError

    def draw_grid(self, grid):
        raise NotImplementedError


class Rectangle(Geometry):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vertices = [(x - width / 2, y - height / 2), (x - width / 2)]
