## Agent 7

## Design

- `Agent7` is expected to catch the prey, not knowing where the prey and predator are exactly in the environment (the agent knows where the predator is in the first timestep only).
    
- Before a node is picked to survey, the probability of the agent node is distributed to the rest of the nodes (since the predator is not present in that node). 
  
- If $\exist i$ such that $P(predator_i) = 1$, the highest probablity of $P(prey_i)$ is surveyed, else the node with highest $P(predator_i)$ is surveyed.

- Probability is distributed the same way as it was done in `Agent 5` and `Agent 3`

- The node with highest $P(predator_i)$ is assumed to be the predator, and the node with the highest $P(prey_i)$ is assumed to be the prey, and the agent moves accordingly.
- After the agent makes its move, the beliefs are propogated to the non-zero beliefs in the dictionary.

- Belief distribution and Transition probabilities remain unchanged from `Agent 3` and `Agent 5`

## Observations

- The agent performs decently well, considering the environment provides only partial information.
- The win rate of the agent is on average 78.43333333%.
- The loss rates are:
    - 0.233333333% due to timeout.
    - 21.33333333% due to death from predator.
- The agent was able to identify the prey node correctly about 0.9898483% of the timesteps.
- The agent was able to identify the predator node correctly about 45.1441661% of the timesteps.

## Inference

- Not knowing where the predator significantly affects the success of the agent, since knowing where the predator means that the agent moves precisely away from the predator.