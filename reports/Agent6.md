## Agent 6

## Design

- `Agent6` is provided with the same conditions as `Agent5`.
- Similar to `Agent2` and `Agent4`, Agent 6 uses the anticipated positions of the prey and predator.

## Implementation

- Agent 6 bootstraps Agent 5. The only change is which nodes are considered as prey and predator when the agent is making a move.
- Agent 6 considers the (immediate) future positions of the prey and predator and chooses the best move based on the rules defined in `Agent1`.
- The anticipated prey position is returned similar to Agent 2: using `predicted_prey_move`, the farthest prey position is considered as the position the prey will move to.
- The anticipated predator move is the next node in the bfs path of the node the predator is believed to be in.

## Observations

- `Agent6` and `Agent5` perform well despite not knowing the position of the predator.
- Agent 6 performs relatively better than Agent 5.
- However they are relatively worse than `Agent3` and `Agent4`.
- The win rate for 150 timesteps is on average 85.8%.
- The loss rates are:
    - 0.066666667% due to timeout.
    - 14.13333333% due to death from predator.
- The agent was able to identify the predator node correctly about 65.3833067% of the timesteps.

## Inference

- The success rates Agent 5 and 6 suffer due to the lack of knowledge of the predator.
- Figuring out the position of the predator is easier than the prey, since its choice of movement is not completely random.