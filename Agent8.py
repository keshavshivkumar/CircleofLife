from Agent7 import Agent7
from env import Node
import random
import global_variables as g_v
import numpy as np
from graph_utils import agent_bfs, bfs, predicted_prey_move
from math import inf

class Agent8(Agent7):
    def __init__(self, node=None) -> None:
        super().__init__(node)
    
    def __str__(self) -> str:
        return '8'
    
    def get_prey_location(self) -> Node:
        node_pos = self.get_random_highest_prey_prob()
        farthest_prey_path = predicted_prey_move(self.node, self.graph_nodes[node_pos])
        future_prey = farthest_prey_path[0]
        return self.graph_nodes[future_prey.pos]

    def move_rulewise(self, prey_node, pred_node):
        curr_dist_from_prey, curr_dist_from_pred = agent_bfs(self.node, prey = prey_node, pred = pred_node)
        # print(f'Pos: {[node.pos for node in curr_dist_from_pred]}, Predator: {pred_node.pos}, Agent: {self.node.pos}, {self.node.predator}')
        # Current positions
        future_prey = curr_dist_from_prey[0] # prey (where it is expected to move) node
        predator = curr_dist_from_pred[0] # pred node
        chosen_neighbor=None
        priority=inf # variable to allow the better neighbor
        for neighbor in self.node.neighbors:
            if neighbor==pred_node:
                continue
            future_pred = bfs(predator, neighbor)[-1]

            path_from_prey = bfs(neighbor, future_prey)
            path_from_pred = bfs(neighbor, future_pred)
            # neighbor is closer to prey
            if len(path_from_prey)<len(curr_dist_from_prey):
                # neighbor is farther from predator
                if len(path_from_pred)>len(curr_dist_from_pred):
                    if priority == 1:
                        chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                    else:
                        priority=1
                        chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred)==len(curr_dist_from_pred):
                    if priority>1:
                        if priority == 2: # breaking ties at random
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=2
                            chosen_neighbor=neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority>6:
                        if priority == 7:
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=7
                            chosen_neighbor=self.node
            # neighbor is not farther from prey
            elif len(path_from_prey)==len(curr_dist_from_prey):
                # neighbor is farther from predator
                if len(path_from_pred)>len(curr_dist_from_pred):
                    if priority>2:
                        if priority == 3:
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=3
                            chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred)==len(curr_dist_from_pred):
                    if priority>3:
                        if priority == 4:
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=4
                            chosen_neighbor=neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority>7:
                        if priority == 8:
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=8
                            chosen_neighbor=self.node
            else:
                # neighbor is farther from predator
                if len(path_from_pred)>len(curr_dist_from_pred):
                    if priority>4:
                        if priority == 5:
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=5
                            chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred)==len(curr_dist_from_pred):
                    if priority>5:
                        if priority == 6:
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=6
                            chosen_neighbor=neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority>8:
                        if priority == 9:
                            chosen_neighbor = random.choice([neighbor, chosen_neighbor])
                        else:
                            priority=9
                            chosen_neighbor=self.node
        self.node.agent=False
        self.node=chosen_neighbor
        self.node.agent=True