# environment for Circle of Life
import random

class Node:
    def __init__(self, pos, agent, prey, predator) -> None:
        self.pos=pos
        self.agent=False
        self.prey=False
        self.predator=False

class Graph:
    def __init__(self) -> None:
        self.numNodes = 50
        # list to store the node objects
        self.graphnodes = [None]
        for i in range(1, self.numNodes+1):
            self.graphnodes.append(Node(i , False, False, False))
        self.graph = dict(zip(self.graphnodes[1:], [None]*self.numNodes))

    def node_selection(self, node: Node):
        x=node.pos
        potential_nodes=[]
        for i in range(x-5, x+6):
            if i < 1:
                temp=50+i
            elif i > 50:
                temp=i-50
            else:
                temp=i
            if temp!=x:
                potential_nodes.append(self.graphnodes[temp])
        # return a random potential node
        return random.choice(potential_nodes)

    def edge_gen(self):
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
    g=Graph()
    graph=g.edge_gen()
    for i, j in graph.items():
        print(i.pos, [x.pos for x in j])

if __name__ == "__main__":
    main()