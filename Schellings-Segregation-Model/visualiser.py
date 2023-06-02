from typing import List, Callable

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk

from simulation import Agent


class Visualiser:
    def __init__(self, agents: List[Agent], update_agents: Callable[[], None]):
        self.agents = agents
        self.update_agents = update_agents
        self.fig, self.ax = plt.subplots()
        self.scatter = self.ax.scatter([], [])
        self.animation = None

    def init_plot(self):
        self.ax.set_xlim(0, 100)  # Set the x-axis limits of the plot
        self.ax.set_ylim(0, 100)  # Set the y-axis limits of the plot
        return self.scatter,

    def update_plot(self, frame):
        for agent in self.agents:
            agent.update()

        x = [agent.x for agent in self.agents]
        y = [agent.y for agent in self.agents]
        self.scatter.set_offsets(list(zip(x, y)))
        return self.scatter,

    def start_simulation(self):
        self.animation = animation.FuncAnimation(
            self.fig, self.update_plot, frames=range(100),
            init_func=self.init_plot, blit=True
        )
        plt.show()
