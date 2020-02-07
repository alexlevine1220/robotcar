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
        env = sensor_data["grid"]

        parent = {}
        cur = (sensor_data["x"], sensor_data["y"])
        q = deque(cur)

        while len(q) != 0:
            (x, y) = q.popleft()
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (env[x + i][y + j] == robotcar.Env.SAFE).all() and (x + i, y + j) not in parent:
                    parent[(x + i, y + j)] = (x, y)
                    q.append((x + i, y + j))

        self.saved_action = deque(cur)

        while cur in parent and parent[cur] != "done":
            if cur[0] == parent[cur][0] + 1:
                self.saved_action.append(Squarebot.RIGHT)
            elif cur[0] == parent[cur][0] - 1:
                self.saved_action.append(Squarebot.LEFT)
            elif cur[1] == parent[cur][1] + 1:
                self.saved_action.append(Squarebot.DOWN)
            elif cur[1] == parent[cur][1] - 1:
                self.saved_action.append(Squarebot.UP)
            cur = parent[cur]

    def act(self, sensor_data):
        if len(self.saved_action) == 0:
            return "LEFT"
        return self.saved_action.pop()


if __name__ == "__main__":
    import os
    sim = robotcar.Simulator("[1]empty.json", debug=True)

    sensor_data, done = sim.reset()
    agent = BfsAgent(sensor_data)

    while True:
        sim.render()
        action = agent.act(sensor_data)
        sensor, done = sim.step("RIGHT")
