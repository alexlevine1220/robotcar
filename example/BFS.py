import robotcar
import random
import time
import math
from collections import deque


class BfsAgent:
    """ Used with circle + birdeye
    """

    def __init__(self, sensor_data):
        self.env = sensor_data

    def bfs(self, start_x, start_y):
        pass

    def act(self, sensor_data):
        return "RIGHT"


if __name__ == "__main__":
    print(dir(robotcar.Robot))
    sim = robotcar.Simulator("SQUARE", {
                             robotcar.Sensor.BIRDEYE}, robotcar.Environment.ENV_1, debug=True)

    sensor_data, done = sim.reset()
    agent = BfsAgent(sensor_data)

    while True:
        sim.render()
        action = agent.act(sensor_data)
        sensor, done = sim.step(action)

        if done:
            break
