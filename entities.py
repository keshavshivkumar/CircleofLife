from abc import abstractmethod
import random
from graph_utils import bfs

class Agent:
    def __init__(self, node = None) -> None:
        self.node = node

    @abstractmethod
    def move(self) -> None:
        pass

class Prey:
    def __init__(self, node) -> None:
        self.node = node
    
    def move(self):
        moveset = list(self.node.neighbors)
        moveset.append(self.node)
        next_node = random.choice(moveset)
        next_node.prey = True
        self.node.prey = False
        self.node = next_node

class Predator:
    def __init__(self, node) -> None:
        self.node = node

    def move(self):
        path = bfs(self.node)
        self.node.predator = False
        self.node = path[-2]
        self.node.predator = True
    