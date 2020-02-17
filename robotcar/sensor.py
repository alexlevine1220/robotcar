from geometry import Line


def create_sensor(config, collision):
    if config["type"] == "BIRDEYE":
        return Birdeye(collision)
    if config["type"] == "LIDAR":
        return Lidar(collision)


class Sensor:
    BIRDEYE = "BIRDEYE"
    RADAR = "RADAR"

    def __init__(self, collision):
        self.collision = collision

    def sense(self, x, y):
        raise NotImplementedError


class Birdeye(Sensor):
    def __init__(self, collision):
        super().__init__(collision)

    def sense(self, x, y):
        return {
            "x": x,
            "y": y,
            "grid": self.collision.map
        }


class Lidar(Sensor, Line):
    def __init__(self, collision):
        self.collision = collision
        
