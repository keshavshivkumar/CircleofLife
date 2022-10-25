from queue import Queue
import random
from math import inf
from secrets import choice

def get_bfs_path(came_from: dict, end_node):
    cur_node = end_node
    path = [cur_node]
    while cur_node != None:
        path.append(came_from[cur_node])
        cur_node = came_from[cur_node]
    return path[:-2]

def pred_bfs(start_node, end_node=None):
    q = Queue()
    q.put(start_node)
    came_from = dict()
    came_from[start_node] = None

    while not q.empty():
        current_node = q.get()

        if end_node is not None:
            if current_node==end_node:
                break
            else:
                pass
        else:
            if current_node.agent:
                break

        for next in current_node.neighbors:
            if next not in came_from:
                q.put(next)
                came_from[next] = current_node
    
    return get_bfs_path(came_from, current_node)

def agent_bfs(start_node):
    q = Queue()
    q.put(start_node)
    came_from = dict()
    came_from[start_node] = None

    prey_node = pred_node = None
    while not q.empty():
        current_node = q.get()
        if current_node.prey:
            prey_node=current_node

        if current_node.predator:
            pred_node=current_node

        if prey_node!=None and pred_node !=None:
            break

        for next in current_node.neighbors:
            if next not in came_from:
                q.put(next)
                came_from[next] = current_node
    
    return get_bfs_path(came_from, prey_node), get_bfs_path(came_from, pred_node)

def predicted_prey_move(agent, node):
    probable_moves=list(node.neighbors)
    probable_moves.append(node)
    choices=[]
    # get second largest distance from agent
    for neighbor_node in probable_moves:
        path=pred_bfs(agent, neighbor_node)
        # print(f'Predicted prey path: {[x.pos for x in path]}')
        choices.append(path)
        # print(agent.pos, neighbor_node.pos, len(path))
    choices.sort(key=lambda x:len(x))
    return choices[-1] # returns largest
    # returns second largest
    '''
    second=choices[-2]
    for i in range(len(choices)):
        if len(choices[i])==second:
            break
    choices=choices[i:-2]
    return random.choice(choices)
    '''
    # predicted_move=random.choice(probable_moves)
    # return predicted_move