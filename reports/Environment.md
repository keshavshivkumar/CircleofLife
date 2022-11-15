# Environment

## Design

- The environment of this project revolves around a `Graph` of 50 nodes. The graph is circular, and the max degree of each node does not exceed 3.
- Edges are randomly generated between nodes besides the adjacent node edges.
- The nodes of the graph are of the `Node` class. Each node has a:
    - position attribute (a number to describe the node number in the graph)
    - agent attribute (if the agent is in that node)
    - prey attribute (if the prey is in that node)
    - predator attribute (if the predator is in that node)
    - neighbor attribute (a set of the node's neighbor)
- The agent is from the `Agent` class. Depending on the environment, there are different implementations of the agent, but all agents have the following attributes in common:
    - node attribute (current position of the agent in the graph)
    - a list of nodes (to keep track of the node positions to maintain probabilities for)
    - ints for storing the correct prey/predator belief, for analysis

## Implementation

- Graph traversal was done using BFS. Using BFS gives the shortest path between 2 nodes.
- The bfs algorithm is the backbone of the agent's and predator's movement. On the other hand, the prey chooses a random position among its neighbor nodes (including its current position) and moves there.
- There are 2 variants of bfs: `bfs()` and `agent_bfs()`. `bfs()` provides the shortest path between 2 nodes, while the latter returns the paths between the agent and the prey & predator.
- Using these paths, the prey and predator nodes are known, and the bfs paths for each of the agent's neighbors to the prey and predator can be found as well.
- With these 4 bfs paths, the agent chooses the optimal neighbor based on the project specifications to move to.