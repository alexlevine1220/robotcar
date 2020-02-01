from robotcar.core import Sensor


class Birdeye(Sensor):
    def __init__(self, env):
        super().__init__(env)

    def sense(self, x, y):
        return
