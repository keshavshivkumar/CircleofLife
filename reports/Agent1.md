## Agent 1

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
- The priority value is set based on the above conditions, implying the lower the priority, the better the choice of neighbor is (lowest priority is 1).
- If there is a tie of priority, the ties are broken at random.

## Observations

- The conditions enable the agent to frequently catch the prey and not die.
- The win rate for 150 timesteps is on average 87.03333333%.
- The loss rates are:
    - 0% due to timeout.
    - 12.96666667% due to death from predator.

## Inference

- In an ideal environment, where the agent has knowledge of where the prey and predator are, it is easy for it to target the prey while also avoiding the predator.
- Another condition could be added to run away from the predator, and the agent will eventually catch the prey. But this will be costly in terms of timesteps.