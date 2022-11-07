from Agent3 import Agent3
from env import Node
import global_variables as g_v
import numpy as np
from graph_utils import bfs, agent_bfs, predicted_prey_move
from math import inf

class Agent4(Agent3):
    def __init__(self, node=None) -> None:
        super().__init__(node)
        self.belief = None
    
    def get_prey_location(self) -> Node:
        node_pos = max(self.belief, key=self.belief.get)
        farthest_prey_path = predicted_prey_move(self.node, self.graph_nodes[node_pos])
        future_prey = farthest_prey_path[0]
        return self.graph_nodes[future_prey.pos]

    def move_rulewise(self, prey_node):
        curr_dist_from_prey, curr_dist_from_pred = agent_bfs(self.node, prey = prey_node)
        # Current positions
        future_prey = curr_dist_from_prey[0] # prey (where it is expected to move) node
        predator = curr_dist_from_pred[0] # pred node
        chosen_neighbor=None
        priority=inf # variable to allow the better neighbor
        for neighbor in self.node.neighbors:
            if neighbor.predator:
                continue
            if neighbor.prey and not neighbor.predator:
                chosen_neighbor=neighbor
                break
            future_pred = bfs(neighbor, predator)[0]
            curr_dist_from_pred = bfs(self.node, future_pred)

            path_from_prey = bfs(neighbor, future_prey)
            path_from_pred = bfs(neighbor, future_pred)
            # neighbor is closer to prey
            if len(path_from_prey)<len(curr_dist_from_prey):
                # neighbor is farther from predator
                if len(path_from_pred)>len(curr_dist_from_pred):
                    priority=1
                    chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred)==len(curr_dist_from_pred):
                    if priority>1:
                        priority=2
                        chosen_neighbor=neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority>6:
                        priority=7
                        chosen_neighbor=self.node
            # neighbor is not farther from prey
            elif len(path_from_prey)==len(curr_dist_from_prey):
                # neighbor is farther from predator
                if len(path_from_pred)>len(curr_dist_from_pred):
                    if priority>2:
                        priority=3
                        chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred)==len(curr_dist_from_pred):
                    if priority>3:
                        priority=4
                        chosen_neighbor=neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority>7:
                        priority=8
                        chosen_neighbor=self.node
            else:
                # neighbor is farther from predator
                if len(path_from_pred)>len(curr_dist_from_pred):
                    if priority>4:
                        priority=5
                        chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred)==len(curr_dist_from_pred):
                    if priority>5:
                        priority=6
                        chosen_neighbor=neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority>8:
                        priority=9
                        chosen_neighbor=self.node
        self.node.agent=False
        self.node=chosen_neighbor
        self.node.agent=True