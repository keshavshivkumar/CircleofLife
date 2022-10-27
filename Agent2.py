from graph_utils import agent_bfs, pred_bfs, predicted_prey_move
from entities import Agent
from math import inf

class Agent2(Agent):
    def __init__(self, node=None) -> None:
        super().__init__(node)
    
    def move(self):
        curr_dist_from_prey, curr_dist_from_pred = agent_bfs(self.node) # paths from current agent node to current prey & predator
        prey = curr_dist_from_prey[0] # prey node
        predator=curr_dist_from_pred[0]
        curr_dist_from_prey = predicted_prey_move(self.node, prey) # path of farthest the prey can move from agent
        curr_dist_from_pred=pred_bfs(self.node, predator)
        chosen_neighbor=None
        priority=inf # variable to allow the better neighbor
        for neighbor in self.node.neighbors:
            if neighbor.prey and not neighbor.predator:
                chosen_neighbor=neighbor
                break
            # _ , path_from_pred = agent_bfs(neighbor)
            path_from_prey = pred_bfs(neighbor, curr_dist_from_prey[0])
            path_from_pred = pred_bfs(neighbor, curr_dist_from_pred[0])
            # neighbor is closer to predicted prey
            if len(path_from_prey) < len(curr_dist_from_prey):
                # neighbor is farther from predator
                if len(path_from_pred) > len(curr_dist_from_pred):
                    priority=1
                    chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred) == len(curr_dist_from_pred):
                    if priority>1:
                        priority=2
                        chosen_neighbor = neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority > 6:
                        priority = 7
                        chosen_neighbor = self.node
            # neighbor is not farther from predicted prey
            elif len(path_from_prey) == len(curr_dist_from_prey):
                # neighbor is farther from predator
                if len(path_from_pred) > len(curr_dist_from_pred):
                    if priority > 2:
                        priority = 3
                        chosen_neighbor=neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred) == len(curr_dist_from_pred):
                    if priority > 3:
                        priority = 4
                        chosen_neighbor = neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority > 7:
                        priority = 8
                        chosen_neighbor = self.node
            else:
                # neighbor is farther from predator
                if len(path_from_pred) > len(curr_dist_from_pred):
                    if priority > 4:
                        priority = 5
                        chosen_neighbor = neighbor
                # neighbor is not closer to predator
                elif len(path_from_pred) == len(curr_dist_from_pred):
                    if priority > 5:
                        priority = 6
                        chosen_neighbor = neighbor
                # neighbor is closer to predator, so sit still
                else:
                    if priority > 8:
                        priority = 9 
                        chosen_neighbor = self.node
        self.node.agent = False
        self.node = chosen_neighbor
        self.node.agent = True