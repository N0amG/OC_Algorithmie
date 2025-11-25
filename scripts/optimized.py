from utils import (
    parse_csv,
    calculate_total_cost,
    calculate_total_profit,
    execution_time,
    ACTIONS_PATH,
    DATASET_1_PATH,
    DATASET_2_PATH,
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
def greedy_algo(actions=parse_csv(ACTIONS_PATH), budget=500):
    # Utiliser l'algorithme du sac à dos pour avoir une solution proche de la meilleur solution

    # filtrer les actions avec un cout negatif ou nul
    actions = [action for action in actions if action[2] > 0]

    # Tri par rentabilité : Profit / Coût
    actions = sorted(actions, key=lambda action: action[2] / action[1], reverse=True)

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


for dataset_path in [DATASET_1_PATH, DATASET_2_PATH]:
    print(f"Résultats pour le fichier : {dataset_path}")
    result = greedy_algo(actions=parse_csv(dataset_path))

    print(
        f"""
    Budget dépensé: {result[1]} €
    Profit total après 2 ans: {result[2]} €
    Actions achetées: {[action[0] for action in result[0]]}
    """
    )
