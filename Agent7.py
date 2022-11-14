import random
from entities import Agent
from env import Node
import global_variables as g_v
import numpy as np
from graph_utils import agent_bfs, bfs
from math import inf

class Agent7(Agent):
    def __init__(self, node=None) -> None:
        super().__init__(node)
        self.prey_belief = None
        self.pred_belief = None

    def __str__(self) -> str:
        return '7'

    def initialize_belief(self):

        #initialize prey belief 1/49
        belief_list = np.zeros(g_v.Number_of_nodes) + 1/(g_v.Number_of_nodes - 1)
        belief_list[self.node.pos] = 0
        self.prey_belief = dict()
        for i,prob in enumerate(belief_list):
            if prob:
                self.prey_belief[i] = prob

        #initialize pred belief with pred location
        self.pred_belief = dict()
        for i in range(g_v.Number_of_nodes):
            if self.graph_nodes[i].predator:
                self.pred_belief[i] = 1

    def propagate_pred_belief(self):
        new_belief = np.zeros(g_v.Number_of_nodes)
        for node_pos in self.pred_belief:
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
            prob = self.pred_belief[node_pos]
            for node in future_positions:
                new_belief[node.pos] += 0.6*prob/len_positions

        for node_pos in self.pred_belief:
            len_positions = self.graph_nodes[node_pos].degree()
            positions = [x.pos for x in self.graph_nodes[node_pos].neighbors]
            for pos in positions:
                new_belief[pos] += 0.4*self.pred_belief[node_pos]/len_positions

        self.pred_belief = dict()
        for i,prob in enumerate(new_belief):
            if prob:
                self.pred_belief[i] = prob

    def propagate_prey_belief(self):
        new_belief = np.zeros(g_v.Number_of_nodes)
        for node_pos in self.prey_belief:
            len_positions = self.graph_nodes[node_pos].degree() + 1
            positions = [x.pos for x in self.graph_nodes[node_pos].neighbors]
            positions.append(node_pos)
            for pos in positions:
                new_belief[pos] += self.prey_belief[node_pos]/len_positions

        self.prey_belief = dict()
        for i,prob in enumerate(new_belief):
            if prob:
                self.prey_belief[i] = prob

    def distribute_prob(self, node_pos, prey = False, pred = False):
        if prey:
            if node_pos not in self.prey_belief:
                return
            prob = self.prey_belief.pop(node_pos)
            denominator = 1-prob

            for node_pos in self.prey_belief:
                self.prey_belief[node_pos] /= denominator

        if pred:
            if node_pos not in self.pred_belief:
                return
            prob = self.pred_belief.pop(node_pos)
            denominator = 1-prob

            for node_pos in self.pred_belief:
                self.pred_belief[node_pos] /= denominator

    def get_random_highest_prey_prob(self):
        max_prob = max(self.prey_belief.values())
        max_belief = dict()
        for node_pos in self.prey_belief:
            if self.prey_belief[node_pos] == max_prob:
                max_belief[node_pos] = max_prob

        return random.choice(list(max_belief.keys()))

    def survey_prey(self):
        node_pos_with_highest_prob = self.get_random_highest_prey_prob()
        if self.graph_nodes[node_pos_with_highest_prob].prey == False:
            self.distribute_prob(node_pos_with_highest_prob, prey=True)
        else:
            self.prey_belief = dict()
            self.prey_belief[node_pos_with_highest_prob] = 1

    def get_close_predators_belief(self, max_prob_belief: dict) -> dict:
        closest_predators = dict()
        min_length = inf
        for node_pos in max_prob_belief:
            curr_pred = self.graph_nodes[node_pos]
            length = len(bfs(curr_pred, self.node))
            if length < min_length:
                closest_predators = dict()
                closest_predators[node_pos] = max_prob_belief[node_pos]
            elif length == min_length:
                closest_predators[node_pos] = max_prob_belief[node_pos]
            
        return closest_predators

    def get_closest_random_pred_node(self) -> int:
        highest_prob = max(self.pred_belief.values())

        max_prob_belief = dict()
        for node_pos in self.pred_belief:
            if self.pred_belief[node_pos] == highest_prob:
                max_prob_belief[node_pos] = highest_prob

        closest_predators = self.get_close_predators_belief(max_prob_belief)

        return random.choice(list(closest_predators.keys()))

    def survey_pred(self):
        node_pos_with_highest_prob = self.get_closest_random_pred_node()
        if self.graph_nodes[node_pos_with_highest_prob].predator == False:
            self.distribute_prob(node_pos_with_highest_prob, pred=True)
        else:
            self.pred_belief = dict()
            self.pred_belief[node_pos_with_highest_prob] = 1

    def survey_node(self):
        self.distribute_prob(self.node.pos, True, True)
        if max(self.pred_belief.values()) < 0.998:
            self.survey_pred()
        else:
            self.survey_prey()

    def get_pred_location(self) -> Node:
        node_pos_with_highest_prob = self.get_closest_random_pred_node()
        return self.graph_nodes[node_pos_with_highest_prob]

    def get_prey_location(self) -> Node:
        node_pos = self.get_random_highest_prey_prob()
        return self.graph_nodes[node_pos]

    def move_rulewise(self, prey_node, pred_node):
        curr_dist_from_prey, curr_dist_from_pred = agent_bfs(self.node, pred = pred_node, prey = prey_node)
        chosen_neighbor=None
        priority=inf # variable to allow the better neighbor
        for neighbor in self.node.neighbors:
            path_from_prey, path_from_pred = agent_bfs(neighbor, pred = pred_node, prey = prey_node)
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
        if self.prey_belief == None or self.pred_belief == None:
            self.initialize_belief()
        # print(f'sum belief {sum(self.pred_belief.values())}')
        self.survey_node()
        prey = self.get_prey_location()
        pred = self.get_pred_location()
        self.move_rulewise(prey_node= prey,pred_node= pred)
        self.propagate_prey_belief()
        self.propagate_pred_belief()