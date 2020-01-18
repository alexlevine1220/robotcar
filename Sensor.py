import math
from Constants import OBSTACLE


class Sensor:
    def __init__(self, env, config):
        """
        :param env: 2d np array where the sensor resides
        :param config: configuration of sensor
        """
        self.env = env

        if config["type"] == "rays":
            self.angle = config["angle"]
            self.n_sensor = config["number"]
            self.range = config["range"]

    def sense(self, x, y):
        """
        :param x: current x position of sensor
        :param y: current y position of sensor
        :return: sensed data
        """
        data = [self.range] * self.n_sensor
        for i in range(self.n_sensor):
            angle = -self.angle / 2 + (self.angle / (self.n_sensor - 1)) * i

            for length in range(self.range):
                ray_x = int(x + math.cos(angle) * length)
                ray_y = int(y + math.sin(angle) * length)

                if (self.env.map[ray_x][ray_y] == OBSTACLE).all():
                    data[i] = length
                    break

        return data
