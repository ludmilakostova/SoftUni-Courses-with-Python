import math
football_player_name = input()
budget = float(input())
beer_cans = int(input())
chips_boxes = int(input())
beer_expenses = 1.20 * beer_cans
chips_expenses = math.ceil(0.45 * beer_expenses * chips_boxes)
total_expenses = beer_expenses + chips_expenses
if budget >= total_expenses:
    print(f'{football_player_name} bought a snack and has {(budget-total_expenses):.2f} leva left.')
else:
    print(f'{football_player_name} needs {abs(budget-total_expenses):.2f} more leva!')
