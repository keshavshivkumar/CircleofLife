# Agent 4

## Design

- `Agent4` is provided with the same conditions as `Agent3`.
- Similar to `Agent2`, Agent 4 uses the anticipated positions of the prey and predator.

## Implementation

- Agent 4 bootstraps off `Agent3` since the probability distribution remains the same.
- The only part that changes is the nodes considered to be where the prey and predator will be after the agent moves.
- The anticipated prey position is returned using `predicted_prey_move` on the node that the prey is believed to be in.
- The anticipated predator position is returned similar to Agent 2: the next node in the bfs path of the predator to the agent's neighbor.

## Observations

- The agent on average knows where the prey is _.
- The win rate is on average _.

## Inference

- In a partial information environment, Agent 4 fares well.
- Both Agent 3 and Agent 4 have reasonably good success rates; knowing where the predator is ensures that the agent will not die that easily.