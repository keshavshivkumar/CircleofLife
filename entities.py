import random
from graph_utils import bfs

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
        self.node = path[0]
        self.node.predator = True
    