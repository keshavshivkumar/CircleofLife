# Agent 7 (with faulty survey and fix)

## Design

- The same design as `Agent 7` but with faulty survey
  
- Let $P(survey_i)$ = $P(prey_i)$ or $P(predator_i)$ depending on what we are surveying for.

- Given that $P(\neg{survey_i}) =0.1$ , $P(survey_i) =0.9$. 

### Belief update

$$P(prey_i| \neg{survey_j}) = {P(prey_i, survey_j) \over{P(\neg{survey_j}) }}$$

$$= {P(prey_i)\times P(\neg{survey_j}| prey_i) \over P(\neg{survey_j})}$$

$$= {P(prey_i)\times P(\neg{survey_j}| prey_i) \over \sum P(prey_i)*p(\neg{survey_j}|prey_i)}$$

$$= { P(prey_i) \times P(\neg{survey_j}| prey_i) \over 1 - P(survey_i) \times P(survey_j)}$$

so we get,
$$P(prey_i| \neg{survey_j}) = { P(prey_i) \times 1 \over 1 - 0.9 \times P(survey_j)}; i \neq j$$

$$P(prey_i| \neg{survey_j}) = { P(prey_i) \times 0.1 \over 1 - 0.9 \times P(survey_j)}; i = j$$

- Transition probabilities remain unchanged from `Agent 7`



## Observations

- The win rate of the agent is on average 58.76666667%.
- The loss rates are:
    - 0% due to timeout.
    - 41.83333333% due to death from predator.
- The agent was able to identify the prey node correctly about 3.298517493% of the timesteps.
- The agent was able to identify the predator node correctly about 37.14797583% of the timesteps.