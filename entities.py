from abc import abstractmethod
import random
from graph_utils import bfs
from env import Node, Graph

class Agent:
    def __init__(self, node = None) -> None:
        self.node: Node = node
        self.graph_nodes: list[Node] = None

    @abstractmethod
    def move(self) -> None:
        pass

class Prey:
    def __init__(self, node = None) -> None:
        self.node = node
    
    def move(self):
        moveset = list(self.node.neighbors)
        moveset.append(self.node)
        next_node = random.choice(moveset)
        self.node.prey = False
        self.node = next_node
        self.node.prey = True

class Predator:
    def __init__(self, node = None) -> None:
        self.node = node

    def move(self):
        path = bfs(self.node)
        self.node.predator = False
        self.node = path.pop()
        self.node.predator = True
    