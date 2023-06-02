from random import random, randint
from typing import List

import matplotlib
from pylab import *

matplotlib.use('TkAgg')

n = 1000    # number of agents
r = 0.1     # neighbourhood radius
th = 0.5    # threshold


class Agent:
    def __init__(self, _type, x, y):
        self.x = x
        self.y = y
        self.type = _type


agents = []


def init_agents():
    global agents
    agents = []
    for i in range(n):
        a = Agent()
        a.type = randint(0, 1)
        a.x = random()
        a.y = random()
        agents.append(a)


def detect_neighbours(ag: Agent) -> List[Agent]:
    """
    The model assumption says each agent checks who are in its neighborhood,
    and if the fraction of the other agents of the same type is less
    than a threshold, it jumps to another randomly selected location.
    exhaustive search: check all agents to see if they are clase enough to
    the focal agent --> ag.
    r --> neighbourhood radius
    """
    global r
    global agents
    return [nb for nb in agents if ((ag.x - nb.x) ** 2 + (ag.y - nb.y) ** 2) < r ** 2 and nb != ag]

import matplotlib.pyplot as plt  # SM 3/28/2020

def observe():
    global agents
    cla()
    white = [ag for ag in agents if ag.type == 0]
    black = [ag for ag in agents if ag.type == 1]
    plot([ag.x for ag in white], [ag.y for ag in white], 'wo')
    plot([ag.x for ag in black], [ag.y for ag in black], 'ko')
    axis('image')
    axis([0, 1, 0, 1])
    plt.show()


def update():
    global agents
    ag = agents[randint(0, n - 1)]
    neighbours = detect_neighbours(ag)
    if len(neighbours) > 0:
        q = len([nb for nb in neighbours if nb.type == ag.type]) / float(len(neighbours))
        if q < th:
            ag.x = random()
            ag.y = random()


# GUI().start(func=[init_agents, observe, update])

while True:
    init_agents()
    update()
    observe()
    for a in agents:
        print(a.x, a.y)