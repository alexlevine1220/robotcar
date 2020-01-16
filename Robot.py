import math


class Robot:
    def __init__(self, robot_type, sensor_type):
        # able to move forward and rotate
        #if robot_type == "basic":
        self.action_space = ["move", "turn_left", "turn_right"]
        self.watching = 0     # in radian between 0, 2 pi
        self.x = 10
        self.y = 190

        self.sensor_type = sensor_type

    def step(self, action):
        """

        :param action:
        :return:
        """
        print(action)
        if action == "move":
            self.x += math.sin(self.watching)
            self.y += math.cos(self.watching)
        elif action == "turn_left":
            self.watching -= 0.1
        elif action == "turn_right":
            self.watching += 0.1


    def reset(self):
        """
        :return:
        sensor  sensor data from robot
        done    0 if not finish, otherwise the number of step taken
        """
        return 0
