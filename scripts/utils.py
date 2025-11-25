import csv

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
