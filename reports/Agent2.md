# Agent 2

## Design

- `Agent2` is provided the same conditions as `Agent1`. How do we make Agent 2 perform better?
- Rather than considering the current positions of the prey and predator, the agent can anticipate where the prey and predator will move in advance.

## Implementation

- The farthest neighbor of the prey is selected as its anticipated move. The path from the agent to that neighbor will cover the other neighbors of the prey as well.
- This is implemented using the `predicted_prey_move` function, and it returns the farthest path of the prey to the agent.
- The anticipated position of the predator will simply be the next node in the bfs path of the predator to the agent's neighbor.

## Observations

- Agent 2 catches the prey more frequently than Agent 1.

## Inference

- In an environment with the necessary information, Agent 2 performs exceptionally well compared to Agent 1.