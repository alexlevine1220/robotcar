import robotcar
from robotcar.robots import Squarebot
import random
import time
import math
from collections import deque


class BfsAgent:
    """ Used with circle + birdeye
    """

    def __init__(self, sensor_data):
        self.map = sensor_data["map"]
        cur = (sensor_data["x"], sensor_data["y"])
        self.parent = {(sensor_data["goal_x"], sensor_data["goal_y"]): "done"}
        self.bfs(cur[0], cur[1])
        self.saved_action = deque(cur)

        while cur in self.parent and self.parent[cur] != "done":
            if cur[0] == self.parent[cur][0] + 1:
                self.saved_action.append(Squarebot.RIGHT)
            elif cur[0] == self.parent[cur][0] - 1:
                self.saved_action.append(Squarebot.LEFT)
            elif cur[1] == self.parent[cur][1] + 1:
                self.saved_action.append(Squarebot.DOWN)
            elif cur[1] == self.parent[cur][1] - 1:
                self.saved_action.append(Squarebot.UP)
            cur = self.parent[cur]

    def bfs(self, start_x, start_y):
        q = deque([(start_x, start_y)])

        while False:  # len(q) != 0:
            (x, y) = q.popleft()
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (self.map[x + i][y + j] == robotcar.Map.SAFE).all() and (x + i, y + j) not in self.parent:
                    self.parent[(x + i, y + j)] = (x, y)
                    q.append((x + i, y + j))

    def act(self, sensor_data):
        if len(self.saved_action) == 0:
            return "move_left"
        return self.saved_action.pop()


if __name__ == "__main__":
    sim = robotcar.Simulator(robotcar.Robot.SQUARE, {
                             robotcar.Sensor.BIRDEYE}, robotcar.Map("empty.json"), debug=True)

    sensor_data, done = sim.reset()
    agent = BfsAgent(sensor_data)

    while True:
        sim.render()
        action = agent.act(sensor_data)
        sensor, done = sim.step("LEFT")
