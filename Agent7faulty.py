import random
from entities import Agent
from env import Node
import global_variables as g_v
import numpy as np
from graph_utils import agent_bfs, bfs
from math import inf
from Agent7 import Agent7

class Agent7Faulty(Agent7):

    def __init__(self, node=None) -> None:
        super().__init__(node)

    def __str__(self) -> str:
        return super().__str__()

    def survey(self, node_pos_with_highest_prob):
        rng = np.random.uniform()

        if self.graph_nodes[node_pos_with_highest_prob].prey == False:
            self.distribute_prob(node_pos_with_highest_prob, prey=True)
        else:
            if rng <= 0.1:
                self.distribute_prob(node_pos_with_highest_prob, prey=True)
            else:
                self.prey_belief = dict()
                self.prey_belief[node_pos_with_highest_prob] = 1
                self.correct_prey_guess+=1

        if self.graph_nodes[node_pos_with_highest_prob].predator == False:
            self.distribute_prob(node_pos_with_highest_prob, pred=True)
        else:
            if rng <= 0.1:
                self.distribute_prob(node_pos_with_highest_prob, pred=True)
            else:
                self.pred_belief = dict()
                self.pred_belief[node_pos_with_highest_prob] = 1
                self.correct_predator_guess+=1

        
