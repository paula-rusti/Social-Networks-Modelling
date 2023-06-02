from random import random, randint
import matplotlib

# matplotlib.use('TkAgg')
from pylab import *

n = 1000  # number of agents
r = 0.1
th = 0.5  # threshold


class Agent:
    pass


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
    return agents


def detect_neighbours(ag: Agent):
    """
    The model assumption says each agent checks who are in its neighborhood,
    and if the fraction of the other agents of the same type is less
    than a threshold, it jumps to another randomly selected location.
    exhaustive search: check all agents to see if they are clase enough to
    the focal agent --> ag.
    r --> neighbourhood radius
    """
    global r
    neighbours = [nb for nb in agents if (ag.x - nb.x) ** 2 + (ag.y - nb.y) ** 2 < r ** 2 and nb != ag]
    return neighbours


def observe():
    global agents
    cla()
    white = [ag for ag in agents if ag.type == 0]
    black = [ag for ag in agents if ag.type == 1]
    plot([ag.x for ag in white], [ag.y for ag in white], 'wo')
    plot([ag.x for ag in black], [ag.y for ag in black], 'ko')
    axis('image')
    axis([0, 1, 0, 1])


def update():
    global agents
    ag = agents[randint(0, n - 1)]
    neighbours = detect_neighbours(ag)
    if len(neighbours) > 0:
        q = len([nb for nb in neighbours if nb.type == ag.type]) / float(len(neighbours))
        if q < th:
            ag.x = random()
            ag.y = random()


from pycxsimulator import GUI


GUI().start(func=[init_agents, observe, update])
