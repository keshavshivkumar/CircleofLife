# Agent 1

## Design

- `Agent1` knows the locations of the prey and predator in the graph. Using the locations of both, the agent makes its move towards the optimal neighbor.
- The optimal neighbor is based on the following order of preference:
    1. Closer to the Prey, farther from the Predator
    2. Closer to the prey, not closer to the Predator
    3. Not farther from the Prey, farther from the Predator
    4. Not farther from the Prey, not closer to the Predator
    5. Farther from the predator
    6. Not closer to the predator
- If the above are not satisfied, the agent does not move and hopefully survives.

## Implementation

- A priority variable is set to infinity. This priority variable chooses the best agent neighbor based on how low it becomes.
- 