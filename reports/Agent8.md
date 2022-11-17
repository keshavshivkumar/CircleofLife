## Agent 8

## Design

- `Agent8` is put in the same environment as `Agent7`, with minimal knowledge of the prey and the predator.
- The agent only knows where the predator is in the first timestep, and has no knowledge of the prey.
- Similar to `Agent2`, `Agent4` and `Agent6`, Agent 8 uses the anticipated positions of the prey and predator.

## Implementation

- Agent 8 boostraps Agent 7, like the other even-numbered agents.
- The anticipated positions of the believed prey and predator are considered for the agent to move.

## Observations

- Agent 8 performs neck-to-neck with Agent 7. Both perform considerably well.
- When the timesteps are more, Agent 8 performs relatively better than Agent7.
- The win rate for 150 timesteps is on average 79.53333333%.
- The loss rates are:
    - 0.466666667% due to timeout.
    - 20% due to death from predator.
- The agent was able to identify the prey node correctly about 1.7391908% of the timesteps.
- The agent was able to identify the predator node correctly about 47.824446% of the timesteps.

## Inference

- Not knowing where the predator significantly affects the success of the agent, since knowing where the predator means that the agent moves precisely away from the predator.
- Not knowing where both the prey and predator are minimizes the gap of success between Agent 7 and Agent 8.