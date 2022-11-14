import copy
from time import perf_counter
from env import Graph
from entities import Predator, Prey, Agent, DistractedPredator
from Agent1 import Agent1
from Agent2 import Agent2
from Agent3 import Agent3
from Agent4 import Agent4
from Agent5 import Agent5
from Agent6 import Agent6
from Agent7 import Agent7
from Agent8 import Agent8
import numpy as np

class Game:
    def __init__(self, agent: Agent, graph: Graph) -> None:
        self.agent = agent
        self.prey = Prey()
        self.predator = Predator()
        if agent.__str__() in '5678':
            self.predator = DistractedPredator()
        self.graph = graph
        self.graph.spawn_entities(self.agent, self.prey, self.predator)
        self.agent.graph_nodes = graph.graph_nodes
        self.maxtimestep = 100
        self.timestep = 0
        self.victory = (False, False)

    def running(self):
        if self.agent.node.predator:
            self.victory = (False, True)
            return False
        if self.agent.node.prey:
            self.victory = (True, True)
            return False
        if self.timestep == self.maxtimestep:
            self.victory = (True, False)
            return False

        return True

    def run(self):
        '''
        Update graph at every timestep
        '''
        while(self.running()):
            self.timestep += 1
            self.agent.move()
            if not self.running():
                break
            self.prey.move()
            self.predator.move()

        return self.victory

def run_game(agent):
    graph = Graph()
    game = Game(agent, graph)
    return game.run()

if __name__ == "__main__":
    a = perf_counter()
    num_agents = 2
    win = np.zeros(num_agents)
    loss2 = np.zeros(num_agents)
    for _ in range(100):
        victories = []
        # [Agent1(), Agent2(), Agent3(), Agent4(), Agent5(), Agent6(), Agent7(), Agent8()]
        agents = [Agent7(), Agent8()]
        for agent in agents:
            v = run_game(agent)
            victories.append(v)
        for i,victory in enumerate(victories):
            if False not in victory:
                win[i] +=1
            elif victory[1] == False:
                loss2[i] +=1

    for w,l2 in zip(win,loss2):
        print(f"win: {w}")
        print(f"loss from timeout: {l2}")
        print()
    b = perf_counter()

    print(f"time taken:{b-a}")