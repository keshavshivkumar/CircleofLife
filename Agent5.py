from entities import Agent
from env import Node
import global_variables as g_v
import numpy as np
from graph_utils import agent_bfs, bfs
from math import inf

class Agent5(Agent):
    def __init__(self, node=None) -> None:
        super().__init__(node)
        self.belief = None

    def initialize_belief(self):
        belief_list = np.zeros(g_v.Number_of_nodes) + 1/(g_v.Number_of_nodes - 1)
        belief_list[self.node.pos] = 0
        self.belief = dict()
        for i,prob in enumerate(belief_list):
            if prob:
                self.belief[i] = prob

    def propagate_pred_belief(self):
        new_belief = np.zeros(g_v.Number_of_nodes)
        for node_pos in self.belief:
            curr_pred_node = self.graph_nodes[node_pos]

            future_positions: list[Node] = []
            min_length = inf
            for neighbor in curr_pred_node.neighbors:
                length = len(bfs(neighbor, self.node))
                if length < min_length:
                    future_positions = [neighbor]
                    min_length = length
                elif length == min_length:
                    future_positions.append(neighbor)

            len_positions = len(future_positions)
            prob = self.belief[node_pos]
            for node in future_positions:
                new_belief[node.pos] += prob/len_positions

        self.belief = dict()
        for i,prob in enumerate(new_belief):
            if prob:
                self.belief[i] = prob
    
    def distribute_prob(self, node_pos):
        if node_pos not in self.belief:
            return
        prob = self.belief.pop(node_pos)
        denominator = 1-prob

        for node_pos in self.belief:
            self.belief[node_pos] /= denominator
        
    def survey_node(self):
        self.distribute_prob(self.node.pos)

        node_pos_with_highest_prob = max(self.belief, key=self.belief.get)
        if self.graph_nodes[node_pos_with_highest_prob].predator == False:
            self.distribute_prob(node_pos_with_highest_prob)
        else:
            self.belief = dict()
            self.belief[node_pos_with_highest_prob] = 1

    def get_pred_location(self) -> Node:
        node_pos = max(self.belief, key=self.belief.get)
        return self.graph_nodes[node_pos]

    def move_rulewise(self, pred_node):
        curr_dist_from_prey, curr_dist_from_pred = agent_bfs(self.node, pred = pred_node)
        chosen_neighbor=None
        priority=inf # variable to allow the better neighbor
        for neighbor in self.node.neighbors:
            path_from_prey, path_from_pred = agent_bfs(neighbor, pred = pred_node)
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

    def move(self):
        if self.belief == None:
            self.initialize_belief()
        
        self.survey_node()
        pred = self.get_pred_location()
        self.move_rulewise(pred)
        self.propagate_pred_belief()