budget = float(input())
number_of_extras = int(input())
price_per_outfit = float(input())
decor = 0.1 * budget
if number_of_extras <= 150:
    expense_outfit = number_of_extras * price_per_outfit
else:
    expense_outfit = number_of_extras * 0.9 * price_per_outfit
total_expenses = decor + expense_outfit
if total_expenses > budget:
    needed_money = abs(budget - total_expenses)
    print("Not enough money!")
    print(f'Wingard needs {needed_money:.2f} leva more.')
elif total_expenses <= budget:
    extra_money = budget - total_expenses
    print("Action!")
    print(f"Wingard starts filming with {extra_money:.2f} leva left.")
