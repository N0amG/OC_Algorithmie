from utils import parse_csv, calculate_total_cost, calculate_total_profit, ACTIONS_PATH

"""
Contraintes:
- Chaque action ne peut être achetée qu'une seule fois.
- Ne peux pas acheter une fraction d'action.
- Le budget maximum est de 500 euros.

Objectif:
- Maximiser le profit total après 2 ans.
- Tester toutes les combinaisons possibles d'achats d'actions.
"""


def greedy_algo(actions=parse_csv(ACTIONS_PATH), budget=500):
    # Utiliser l'algorithme du sac à dos pour avoir une solution proche de la meilleur solution

    # Tri par rentabilité : Profit / Coût
    actions = sorted(actions, key=lambda action: action[2] / action[1], reverse=True)
    print(actions)

    combinations = []

    for action in actions:
        if calculate_total_cost(combinations) + action[1] <= budget:
            combinations.append(action)
        else:
            continue
    return (
        combinations,
        calculate_total_cost(combinations),
        calculate_total_profit(combinations),
    )


result = greedy_algo()
print(result)
