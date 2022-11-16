## Agent 3

## Design

- `Agent3` is expected to catch the prey, not knowing where the prey is in the environment, but knowing where the predator is.
- The agent does have the luxury of surveying a node to check if the prey is there.
- Before a node is picked to survey, the probability of the agent node is distributed to the rest of the nodes. The node with the highest probability in the dictionary is picked and is checked for the prey.
    - If the prey is not found, then the belief of that node is distributed.
    - If the prey is found, the belief of that node becomes 1 and the rest of the beliefs become 0.
- The surveyed nodes is assumed to be the prey, and the agent moves accordingly.
- After the agent makes its move, the beliefs are propogated to the non-zero beliefs in the dictionary.
- To generalize, if a node x is picked and surveyed:
    - if the prey is in x, then P(x|prey is in x) = 1 and P(y<sub>i</sub>|prey is in x) = 0
    - if the prey is not in x, then P(x|prey is not in x) = 0, and P(y<sub>i</sub>|prey is not in x) = P(prey is in y<sub>i</sub>, prey is not in x) / P(failed to find prey in x) = P(prey is in y<sub>i</sub>) * P(failed to find prey in prey in x|prey is in y<sub>i</sub>) / P(failed to find prey in x), where y<sub>i</sub> is a neighbor of x.

## Implementation

- In the beginning, all the nodes are provided a probability of 1/49; considering the number of nodes in the graph to be 50, and the number of nodes the prey can be in is 49 (the agent is already in a node, so the prey can't be there). This is carried out by the `initialize_belief` function.
- The beliefs are stored in a dictionary of the `Agent3` class. Only the nodes with non-zero belief are stored in the dictionary.
- The agent surveys a node using `survey_node()`.
- If the node has the prey, then the dictionary is reset and only that node is added to the dictionary with a probability of 1.
- Otherwise, the node picked gets removed from the belief dictionary, and its probability is distributed to the rest of the nodes.
- The agent moves assuming the node to have the prey, and follows the set of rules defined in `Agent1` (the location of the predator is known).
- The belief of the position the agent moves to is propogated to the rest of the nodes in the belief dictionary.

## Observations

- The agent performs considerably well, considering the environment provides only partial information.
- The win rate of the agent is on average _.
- The agent was able to identify the prey node correctly about _% of the timesteps

## Inference

- Not knowing where the prey is does not affect the success of the agent, since knowing where the predator is means that the agent moves precisely away from the predator as much as possible.
- It is difficult to keep track of the prey once discovered, since its movement is random.