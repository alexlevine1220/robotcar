import random
import time
import math

from Constants import BLANK
from Simulator import Simulator
from collections import deque


class BfsAgent:
    """ Used with circle + birdeye

    Arguments:
        object {} -- [description]

    Returns:
        [type] -- [description]
    """

    def __init__(self, action_space, env):
        self.action_space = action_space
        self.env = env
        self.count = 0
        self.parent = {(env.start_x, env.start_y): "done"}
        self.bfs(env.start_x, env.start_y)
        # should be (env.goal_x, env.goal_y)
        cur = (95, 127)
        self.saved_action = deque()
        self.saved_action.append(cur)
        print(self.parent)
        while cur in self.parent and self.parent[cur] != "done":
            if cur[0] == self.parent[cur][0] + 1:
                self.saved_action.append("move_right")
            elif cur[0] == self.parent[cur][0] - 1:
                self.saved_action.append("move_left")
            elif cur[1] == self.parent[cur][1] + 1:
                self.saved_action.append("move_down")
            elif cur[1] == self.parent[cur][1] - 1:
                self.saved_action.append("move_up")
            else:
                self.saved_action.append("ERROR")
            cur = self.parent[cur]
        print(self.saved_action)

    def bfs(self, start_x, start_y):
        q = deque([(start_x, start_y)])

        while len(q) != 0:
            (x, y) = q.popleft()
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if self.env.type(x + i, y + j) in {"SAFE", "GOAL"} and (x + i, y + j) not in self.parent:
                    self.parent[(x + i, y + j)] = (x, y)
                    q.append((x + i, y + j))

    def act(self):
        if len(self.saved_action) == 0:
            return "move_left"
        return self.saved_action.pop()


class RandomAgent:
    """[summary]

    Returns:
        [type] -- [description]
    """

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, sensor):
        return random.choice(self.action_space)


if __name__ == "__main__":
    sim = Simulator("square", "birdeye", "images/maze00.jpg")

    sensor_data, done = sim.reset()
    agent = BfsAgent(sim.action_space, sim.env)

    sim.reset()
    while True:
        print("tick")
        sim.render()
        action = agent.act()
        sensor, done = sim.step(action)

        if done:
            break

    sim.close()
