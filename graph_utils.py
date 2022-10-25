from queue import Queue
import random
from math import inf

def get_bfs_path(came_from: dict, end_node):
    cur_node = end_node
    path = [cur_node]
    while cur_node != None:
        path.append(came_from[cur_node])
        cur_node = came_from[cur_node]
    return path[:-1]

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
    choices=dict()
    # get second largest distance from agent
    for neighbor_node in probable_moves:
        path=pred_bfs(agent, neighbor_node)
        print(f'Predicted prey path: {[x.pos for x in path]}')
        # print(agent.pos, neighbor_node.pos, len(path))
        choices[len(path)] = path
    max_dist=max(zip(choices.keys(), choices.values()))
    min_dist=min(zip(choices.keys(), choices.values()))
    for i, j in choices.items():
        if i<max_dist[0]:
            if i>min_dist[0]:
                min_dist=(i,j)
            elif i==min_dist[0]:
                cointoss=random.choice([0,1])
                if cointoss==0:
                    min_dist=(i,j)
    return min_dist[1]
    # predicted_move=random.choice(probable_moves)
    # return predicted_move