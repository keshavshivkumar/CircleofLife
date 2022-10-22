from queue import Queue

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

    while not q.empty():
        current_node = q.get()

        if current_node.prey:
            prey_node=current_node

        if current_node.predator:
            pred_node=current_node

        if prey_node and pred_node:
            break

        for next in current_node.neighbors:
            if next not in came_from:
                q.put(next)
                came_from[next] = current_node
    
    return get_bfs_path(came_from, prey_node), get_bfs_path(came_from, pred_node)