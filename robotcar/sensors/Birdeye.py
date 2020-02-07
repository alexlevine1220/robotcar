from robotcar.core import Sensor


class Birdeye(Sensor):
    def __init__(self, map):
        super().__init__(map)

    def sense(self, x, y):
        return {
            "x": x,
            "y": y,
            "goal_x": self._map.goal_x,
            "goal_y": self._map.goal_y,
            "grid": self._map.grid
        }
