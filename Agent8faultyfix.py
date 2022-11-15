import random
from entities import Agent
from env import Node
import global_variables as g_v
import numpy as np
from graph_utils import agent_bfs, bfs
from math import inf
from Agent8faulty import Agent8Faulty

class Agent8FaultyFix(Agent8Faulty):

    def __init__(self, node=None) -> None:
        super().__init__(node)

    def __str__(self) -> str:
        return super().__str__()

    def distribute_prob(self, node_pos, prey = False, pred = False):
        if prey and node_pos in self.prey_belief:
            prob = self.prey_belief[node_pos]
            denominator = 1-0.9*prob

            for pos in self.prey_belief:
                if pos == node_pos:
                    self.prey_belief[pos] = self.prey_belief[pos]*0.1/denominator
                else:
                    self.prey_belief[pos] /= denominator

        if pred and node_pos in self.pred_belief:
            prob = self.pred_belief[node_pos]
            denominator = 1-0.9*prob

            for pos in self.pred_belief:
                if pos == node_pos:
                    self.pred_belief[pos] = self.pred_belief[pos]*0.1/denominator
                else:
                    self.pred_belief[pos] /= denominator

        
