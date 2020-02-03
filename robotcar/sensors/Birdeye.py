from robotcar.core import Sensor


class Birdeye(Sensor):
    def __init__(self, env):
        super().__init__(env)
        self.map = env.get_map

    def sense(self, x, y):
        return self.map
