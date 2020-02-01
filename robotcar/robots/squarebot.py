from robotcar.core import Robot


class Squarebot(Robot):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

    def __init__(self, env, sensors, start_x, start_y):
        super().__init__(env, sensors, start_y, start_y)
        self.action_space = {Squarebot.LEFT,
                             Squarebot.RIGHT, Squarebot.UP, Squarebot.DOWN}

    def step(self, action):
        if action == Squarebot.LEFT:
            self._x -= 1
        if action == Squarebot.RIGHT:
            self._x += 1
        if action == Squarebot.UP:
            self._y += 1
        if action == Squarebot.DOWN:
            self._y -= 1
