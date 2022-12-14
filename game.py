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
from Agent7faulty import Agent7Faulty
from Agent8faulty import Agent8Faulty
from Agent7faultyfix import Agent7FaultyFix
from Agent8faultyfix import Agent8FaultyFix
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
        self.maxtimestep = 50
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
            if not self.running(): # in case the prey moves into the agent's node
                break
            self.predator.move()
        return self.victory, self.timestep

def run_game(agent):
    graph = Graph()
    game = Game(agent, graph)
    return game.run()

if __name__ == "__main__":
    a = perf_counter()
    num_agents = 8
    iterations=100
    win = np.zeros(num_agents)
    loss2 = np.zeros(num_agents)
    agent_caught = np.zeros(num_agents)
    for _ in range(iterations):
        victories = []
        # [Agent1(), Agent2(), Agent3(), Agent4(), Agent5(), Agent6(), Agent7(), Agent8(), Agent7Faulty(), Agent8Faulty(), Agent7FaultyFix(), Agent8FaultyFix()]
        agents = [Agent1(), Agent2(), Agent3(), Agent4(), Agent5(), Agent6(), Agent7(), Agent8()]
        correct_prey_guess={agent:0 for agent in agents}
        correct_predator_guess={agent:0 for agent in agents}
        for agent in agents:
            v, timesteps = run_game(agent)
            victories.append(v)
            prey_guess_rate=agent.correct_prey_guess/timesteps
            predator_guess_rate=agent.correct_predator_guess/timesteps
            correct_prey_guess[agent]+=prey_guess_rate
            correct_predator_guess[agent]+=predator_guess_rate

        for i,victory in enumerate(victories):
            if False not in victory:
                win[i] += 1
            elif victory[1] == False:
                loss2[i] += 1
            elif victory[0] == False:
                agent_caught[i] += 1

    for w, l2, death, agent in zip(win, loss2, agent_caught, agents):
        print()
        print(f"win percentage: {(w/iterations)*100}")
        print(f"loss from timeout: {(l2/iterations)*100}")
        print(f"agent caught by predator: {(death/iterations)*100}")
        print(f"Accuracy of prey guess over timesteps: {(correct_prey_guess[agent]/iterations)*100}")
        print(f"Accuracy of predator guess over timesteps: {(correct_predator_guess[agent]/iterations)*100}")
    print()
    b = perf_counter()

    print(f"time taken:{b-a}")