## Agent 5

## Design

- `Agent5` is expected to catch the prey, not knowing where the predator is exactly in the environment (the agent only knows in the first timestep where the predator is).
    
- Before a node is picked to survey, the probability of the agent node is distributed to the rest of the nodes (since the predator is not present in that node). 
  
- Let ${predator_i} =$ predator present in Node $i$ according to survey
  
- The node with the highest probability $P(predator_i)$ is picked and is surveyed.
    - If the predator is not found, then the belief of that node is distributed.
    - If the predator is found, the belief of that node becomes 1 and the rest of the beliefs become 0.


- The node with highest $P(predator_i)$ is assumed to be the predator, and the agent moves accordingly.
- After the agent makes its move, the beliefs are propogated to the non-zero beliefs in the dictionary.

### Belief Distribution
$$ 
    P(predator_i| \neg{predator_j}) = {P(predator_i, predator_j)\over P(\neg{predator_j}) }
    ; i \neq j
$$
 
$$ 
    = {P(predator_i)\times P(\neg{predator_j}| predator_i) \over P(\neg{predator_j})}
$$

$$
    = {
        P(predator_i)\times 1 \over 
        \sum P(predator_i)*p(\neg{predator_j}|predator_i)
    }
$$

$$
    = { P(predator_i) \over 1 - P(predator_j)}
$$

- If $P(predator_i) = 1$, then $P(predator_j) = 0$, $\forall j$, ${j \neq i }$

### Transition Update
- Distracted Predator moves to close in distance to agent at Prob = 0.6, $P(optimal) = 0.6$. It moves randomly to any of its neighbors at Prob = 0.4, $P(distracted) = 0.4$
$$
    P(predator_{i}) = 
        \sum_{k=1}^{n} P(Predator_{k}) \times P(predator_{i}|predator_k)
    
$$

$$
    = 0.6 \sum_{k=1}^{n} optimal(P(predator_i|predator_j))
$$
$$
    +
    0.4\sum_{k=1}^{n} distracted(P(predator_i|predator_j))
$$
where $P(predator_i|predator_k) =$ Probability of moving to Node $i$ from Node $k$.

## Implementation

- In the beginning, the agent knows where the predator is and prob of that node is initialized to 1. This is carried out by the `initialize_belief_with_position` function.

- The beliefs are stored in a dictionary of the `Agent5` class. Only the nodes with non-zero belief are stored in the dictionary.
  
- The agent surveys a node using `survey_node()`.
- If the predator is present in that node, then the dictionary is reset and only that node is added to the dictionary with a probability of 1.
- Otherwise, the node picked gets removed from the belief dictionary, and its probability is distributed to the rest of the nodes.
- The agent moves assuming the node with highest $P(predator_i)$ to have the predator, and follows the set of rules defined in `Agent1` (the location of the prey is known).
- The belief of the predator is propogated to the rest of the nodes in the belief dictionary.

## Observations

- The agent performs decently well, considering the environment provides only partial information.
- The win rate for 150 timesteps is on average 80.63333333%.
- The loss rates are:
    - 0% due to timeout.
    - 19.36666667% due to death from predator.
- The agent was able to identify the predator node correctly about 58.0649433% of the timesteps.

## Inference

- Not knowing where the predator significantly affects the success of the agent, since knowing where the predator means that the agent moves precisely away from the predator.
- Figuring out the position of the predator is easier than the prey, since its choice of movement is not completely random.