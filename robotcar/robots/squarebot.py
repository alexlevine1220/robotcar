from robotcar.core import Robot, ROBOT


class SquareBot(Robot):
    def __init__(self, robot_type, sensor_types):
        self.robot_type = ROBOT.SQUARE
        self.sensors = {}
