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
        self.parent = {(sim.env.start_x, sim.env.start_y): "done"}
        self.bfs(sim.env.start_x, sim.env.start_y)
        # should be (env.goal_x, env.goal_y)
        cur = (300, 210)
        self.saved_action = deque()
        self.saved_action.append(cur)
        while cur in self.parent and self.parent[cur] != "done":
            if cur[0] == self.parent[cur][0] + 1:
                self.saved_action.append("move_right")
            elif cur[0] == self.parent[cur][0] - 1:
                self.saved_action.append("move_left")
            elif cur[1] == self.parent[cur][1] + 1:
                self.saved_action.append("move_down")
            elif cur[1] == self.parent[cur][1] - 1:
                self.saved_action.append("move_up")
            cur = self.parent[cur]

    def bfs(self, start_x, start_y):
        q = deque([(start_x, start_y)])

        while len(q) != 0:
            (x, y) = q.popleft()
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if self.env.type(x + i, y + j) == "SAFE" and (x + i, y + j) not in self.parent:
                    self.parent[(x + i, y + j)] = (x, y)
                    q.append((x + i, y + j))

    def act(self, sensor_data):
        if len(self.saved_action) == 0:
            return "move_left"
        return self.saved_action.pop()


if __name__ == "__main__":
    sim = robotcar.Simulator(robotcar.ROBOT.SQUARE, {
                             robotcar.SENSOR.BIRDEYE}, robotcar.ENV.ENV_1, debug=True)

    sensor_data, done = sim.reset()
    agent = BfsAgent(sensor_data)

    while True:
        sim.render()
        action = agent.act(sensor_data)
        sensor, done = sim.step(action)

        if done:
            break
