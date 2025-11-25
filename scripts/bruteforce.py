import csv
import itertools as it

"""
Contraintes:
- Chaque action ne peut être achetée qu'une seule fois.
- Ne peux pas acheter une fraction d'action.
- Le budget maximum est de 500 euros.

Objectif:
- Maximiser le profit total après 2 ans.
- Tester toutes les combinaisons possibles d'achats d'actions.
"""


ACTIONS_PATH = "liste_actions.csv"


def calculate_profit(action):
    """Calculates the profit for a given action over 2 years."""
    price = float(action[1])
    profit_percentage = float(action[2].split("%")[0])
    profit = (price * profit_percentage / 100) * 2
    return profit


def parse_csv(file_path):
    """Reads a CSV file and returns its content as a list of tuples."""
    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        return [tuple([row[0], int(row[1]), calculate_profit(row)]) for row in reader]


def calculate_total_profit(action_combination):
    """Calculates the total profit for a combination of actions."""
    total_profit = 0
    for action in action_combination:
        total_profit += action[2]
    return total_profit


def calculate_total_cost(action_combination):
    """Calculates the total cost for a combination of actions."""
    total_cost = 0
    for action in action_combination:
        total_cost += float(action[1])
    return total_cost


def bruteforce(actions=parse_csv(ACTIONS_PATH), budget=500):
    # Créer une chaine de toutes les possibilités de combinaisons allant de 1 à 20 actions
    all_combinations = it.chain.from_iterable(
        it.combinations(actions, i) for i in range(1, len(actions) + 1)
    )
    valid_combinations = (
        c for c in all_combinations if calculate_total_cost(c) <= budget
    )

    best_combination = max(valid_combinations, key=calculate_total_profit)

    return {
        best_combination,
        calculate_total_cost(best_combination),
        calculate_total_profit(best_combination),
    }


result = bruteforce()
print(result)
