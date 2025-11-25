import itertools as it
from utils import (
    parse_csv,
    calculate_total_cost,
    calculate_total_profit,
    execution_time,
    ACTIONS_PATH,
)

"""
Contraintes:
- Chaque action ne peut être achetée qu'une seule fois.
- Ne peux pas acheter une fraction d'action.
- Le budget maximum est de 500 euros.

Objectif:
- Maximiser le profit total après 2 ans.
- Tester toutes les combinaisons possibles d'achats d'actions.
"""


@execution_time
def bruteforce(actions=parse_csv(ACTIONS_PATH), budget=500):
    # Créer une chaine de toutes les possibilités de combinaisons allant de 1 à 20 actions
    all_combinations = it.chain.from_iterable(
        it.combinations(actions, i) for i in range(1, len(actions) + 1)
    )
    valid_combinations = (
        c for c in all_combinations if calculate_total_cost(c) <= budget
    )

    best_combination = max(valid_combinations, key=calculate_total_profit)

    return (
        best_combination,
        calculate_total_cost(best_combination),
        calculate_total_profit(best_combination),
    )


result = bruteforce()
print(
    f"""
Budget dépensé: {result[1]} €
Profit total après 2 ans: {result[2]} €
Actions achetées: {[action[0] for action in result[0]]}
"""
)
