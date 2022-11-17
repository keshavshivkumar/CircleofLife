# Agent 7 (with faulty survey)

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

- Transition probabilities remain unchanged



## Observations