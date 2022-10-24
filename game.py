from time import perf_counter
from env import Graph
from entities import Predator, Prey, Agent
from Agent1 import Agent1
from Agent2 import Agent2
from math import inf

class Game:
    def __init__(self, agent: Agent, graph: Graph) -> None:
        self.agent = agent
        self.prey = Prey()
        self.predator = Predator()
        self.graph = graph
        self.graph.spawn_entities(self.agent, self.prey, self.predator)
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
            self.predator.move()

        return self.victory

def run_game():
    agent = Agent1()
    graph = Graph()
    game = Game(agent, graph)
    return game.run()
        
if __name__ == "__main__":
    a = perf_counter()
    win = 0
    loss2 = 0
    for _ in range(1):
        victory = run_game()
        if False not in victory:
            win += 1
        elif victory[1] == False:
            loss2 +=1

    print(f"win: {win}")
    print(f"loss from timeout: {loss2}")
    b = perf_counter()

    print(f"time taken:{b-a}")


