# environment for Circle of Life
import random
import global_variables as g_v

class Node:
    def __init__(self, pos, agent = False, prey = False, predator = False) -> None:
        self.pos=pos
        self.agent = agent
        self.prey = prey
        self.predator = predator
        self.neighbors = set()

    def degree(self):
        return len(self.neighbors)

class Graph2:
    def init_nodes(self):
        #create new nodes
        for i in range(self.numNodes):
            new_node = Node(i)
            self.graph_nodes.append(new_node)
    
    def make_circle(self):
        #adds prev and next neighbor to each node
        for i,node in enumerate(self.graph_nodes):
            next_node = (i+1)%g_v.Number_of_nodes
            prev_node = (i-1)%g_v.Number_of_nodes
            node.neighbors.add(self.graph_nodes[next_node])
            node.neighbors.add(self.graph_nodes[prev_node])

    def node_selection(self, node: Node):
        x=node.pos
        potential_nodes=[]
        for i in range(x-5, x+6):
            temp = i % g_v.Number_of_nodes
            temp_node = self.graph_nodes[temp]

            if temp not in [x-1, x, x+1] and temp_node.degree() < 3:
                potential_nodes.append(temp_node)
        
        # return a random potential node
        if potential_nodes != []:
            return random.choice(potential_nodes)
        else:
            return None

    def add_new_edges(self):
        indexes = list(range(g_v.Number_of_nodes))
        while(len(indexes) > 0):
            random_index = random.choice(indexes)
            indexes.remove(random_index)
            curr_node = self.graph_nodes[random_index]

            if curr_node.degree() > 2:
                continue

            choice_node = self.node_selection(curr_node)
            curr_node.neighbors.add(choice_node)
            if choice_node:
                choice_node.neighbors.add(curr_node)

        # remove neigbors valued None
        for node in self.graph_nodes:
            if None in node.neighbors:
                node.neighbors.remove(None)


    def __init__(self) -> None:
        self.numNodes = g_v.Number_of_nodes
        # list to store the node objects
        self.graph_nodes = list()
        self.init_nodes()
        self.make_circle()
        self.add_new_edges()   

class Graph:

    def init_nodes(self):
        #create new nodes
        for i in range(self.numNodes):
            new_node = Node(i)
            self.graph_nodes.append(new_node)

        #make circle
        for i,node in enumerate(self.graph_nodes):
            next_node = (i+1)%g_v.Number_of_nodes
            prev_node = (i-1)%g_v.Number_of_nodes
            node.neighbors.add(next_node)
            node.neighbors.add(prev_node)

    def __init__(self) -> None:
        self.numNodes = g_v.Number_of_nodes
        # list to store the node objects
        self.graphnodes = [None]
        for i in range(1, self.numNodes+1):
            self.graphnodes.append(Node(i))
        self.graph = dict(zip(self.graphnodes[1:], [None]*self.numNodes))

    def node_selection(self, node: Node):
        x=node.pos
        potential_nodes=[]
        for i in range(x-5, x+6):
            if i < 1:
                temp=g_v.Number_of_nodes+i
            elif i > g_v.Number_of_nodes:
                temp=i-g_v.Number_of_nodes
            else:
                temp=i
            if temp!=x:
                potential_nodes.append(self.graphnodes[temp])
        # return a random potential node
        return random.choice(potential_nodes)

    def edge_gen(self) -> dict():
        # generate a circular undirected graph
        self.graph[self.graphnodes[1]] = [self.graphnodes[self.numNodes], self.graphnodes[2]]
        for i in range(2, self.numNodes):
            self.graph[self.graphnodes[i]] = [self.graphnodes[i-1], self.graphnodes[i+1]]
        self.graph[self.graphnodes[self.numNodes]] = [self.graphnodes[self.numNodes-1], self.graphnodes[1]]

        # add random edges based on the condition
        for i in range(1, self.numNodes+1):
            new_edge=self.node_selection(self.graphnodes[i])
            # check if the current node and the potential node each have a degree of less than 3
            if len(self.graph[self.graphnodes[i]])<3 and len(self.graph[new_edge])<3:
                # make sure the potential node isn't already in the current node's edge list and vice versa
                if new_edge not in self.graph[self.graphnodes[i]] and self.graphnodes[i] not in self.graph[new_edge]:
                    self.graph[self.graphnodes[i]].append(new_edge)
                    self.graph[new_edge].append(self.graphnodes[i])
        return self.graph

def main():
    g = Graph2()
    # graph = g.edge_gen()
    # for i, j in graph.items():
    #     print(i.pos, [x.pos for x in j])

    for node in g.graph_nodes:
        print(f"{node.pos}: ({[x.pos for x in node.neighbors]})")

if __name__ == "__main__":
    main()