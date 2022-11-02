from abc import abstractmethod
import random
from turtle import pos
from graph_utils import bfs
from env import Node, Graph
from math import inf

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
        min_length = inf
        positions = []
        for neighbor in self.node.neighbors:
            path = bfs(neighbor)
            if len(path) < min_length:
                positions = [neighbor]
                min_length = len(path)
            elif len(path) == min_length:
                positions.append(neighbor)
        
        position = random.choice(positions)
        self.node.predator = False
        self.node = position
        self.node.predator = True
    