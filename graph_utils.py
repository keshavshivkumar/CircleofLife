from queue import Queue
import random

def get_bfs_path(came_from: dict, end_node):
    cur_node = end_node
    path = [cur_node]
    while cur_node != None:
        path.append(came_from[cur_node])
        cur_node = came_from[cur_node]
    return path

def pred_bfs(start_node):
    q = Queue()
    q.put(start_node)
    came_from = dict()
    came_from[start_node] = None

    while not q.empty():
        current_node = q.get()

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
    prey_path=predator_path=[]

    while not q.empty():
        current_node = q.get()
        if current_node.prey:
            prey_node=current_node
            if not prey_path:
                prey_path=get_bfs_path(came_from, prey_node)

        if current_node.predator:
            pred_node=current_node
            if not predator_path:
                predator_path=get_bfs_path(came_from, pred_node)

        if prey_node!=None and pred_node !=None:
            break

        for next in current_node.neighbors:
            if next not in came_from:
                q.put(next)
                came_from[next] = current_node
    
    return prey_path, predator_path

def predicted_prey_move(node):
    probable_moves=list(node.neighbors)
    probable_moves.append(node)
    predicted_move=random.choice(probable_moves)
    return predicted_move

def agent2_bfs(start_node, next_prey_move):
    q = Queue()
    q.put(start_node)
    came_from = dict()
    came_from[start_node] = None

    while not q.empty():
        current_node = q.get()

        if current_node == next_prey_move:
            break

        for next in current_node.neighbors:
            if next not in came_from:
                q.put(next)
                came_from[next] = current_node
    
    return get_bfs_path(came_from, current_node)