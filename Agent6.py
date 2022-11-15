from Agent5 import Agent5
from env import Node
import global_variables as g_v
import numpy as np
from graph_utils import bfs, agent_bfs, predicted_prey_move
from math import inf
import random

class Agent6(Agent5):
    def __init__(self, node=None) -> None:
        super().__init__(node)
        self.belief = None
    
    def __str__(self) -> str:
        return '6'

    def move_rulewise(self, pred_node):
        curr_dist_from_prey, curr_dist_from_pred = agent_bfs(self.node, pred = pred_node)
        # Current positions
        prey = curr_dist_from_prey[0] # prey node
        predator = pred_node # pred node

        # Predicted prey position
        curr_dist_from_prey = predicted_prey_move(self.node, prey) # path of farthest the prey can move from agent
        future_prey = curr_dist_from_prey[0]

        chosen_neighbor=None
        priority=inf # variable to allow the better neighbor
        for neighbor in self.node.neighbors:
            if neighbor==predator: # if the neighbor is the predicted predator
                continue
            
            future_pred = bfs(predator, neighbor)[-1]
            # print(f'Predator path: {[x.pos for x in future_pred]}')
            # curr_dist_from_pred = bfs(self.node, future_pred)

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