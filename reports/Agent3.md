## Agent 3

## Design

- `Agent3` is expected to catch the prey, not knowing where the prey is in the environment, but knowing where the predator is.
  
- The agent does have the luxury of surveying a node to check if the prey is there.

  
- Before a node is picked to survey, the probability of the agent node is distributed to the rest of the nodes (since the prey is not present in that node). 
  
- Let ${prey_i} =$ Prey present in Node $i$ according to survey
  
- The node with the highest probability $P(Prey_i)$ is picked and is surveyed.
    - If the prey is not found, then the belief of that node is distributed.
    - If the prey is found, the belief of that node becomes 1 and the rest of the beliefs become 0.


- The node with highest $P(Prey_i)$ is assumed to be the prey, and the agent moves accordingly.
- After the agent makes its move, the beliefs are propogated to the non-zero beliefs in the dictionary.

### Belief Distribution
$$ 
    P(prey_i| \neg{prey_j}) = {P(prey_i, prey_j)\over P(\neg{prey_j}) }
    ; i \neq j
$$
 
$$ 
    = {P(prey_i)\times P(\neg{prey_j}| prey_i) \over P(\neg{prey_j})}
$$

$$
    = {
        P(prey_i)\times 1 \over 
        \sum P(prey_i)*p(\neg{prey_j}|prey_i)
    }
$$

$$
    = { P(prey_i) \over 1 - P(prey_j)}
$$

- If $P(prey_i) = 1$, then $P(prey_j) = 0$, $\forall j$, ${j \neq i }$

### Transition Update

$$
    P(prey_{i}) = {
        \sum_{k=1}^{n} P(prey_k) \times P(prey_{i}|prey_k)
    }
$$
where $P(prey_i|prey_k) =$ Probability of moving to Node $i$ from Node $k$

## Implementation

- In the beginning, all the nodes are provided a probability of 1/49; considering the number of nodes in the graph to be 50, and the number of nodes the prey can be in is 49 (the agent is already in a node, so the prey can't be there). This is carried out by the `initialize_belief` function.
- The beliefs are stored in a dictionary of the `Agent3` class. Only the nodes with non-zero belief are stored in the dictionary.
- The agent surveys a node using `survey_node()`.
- If the prey is present in that node, then the dictionary is reset and only that node is added to the dictionary with a probability of 1.
- Otherwise, the node picked gets removed from the belief dictionary, and its probability is distributed to the rest of the nodes.
- The agent moves assuming the node with the highest $P(prey_i)$ to have the prey, and follows the set of rules defined in `Agent1` (the location of the predator is known).
- The belief of the prey to is propogated to the rest of the nodes in the belief dictionary.

## Observations

- The agent performs considerably well, considering the environment provides only partial information.
- The win rate of the agent is on average _.
- The agent was able to identify the prey node correctly about _% of the timesteps

## Inference

- Not knowing where the prey is does not affect the success of the agent, since knowing where the predator is means that the agent moves precisely away from the predator as much as possible.
- It is difficult to keep track of the prey once discovered, since its movement is random.