expected_profit = float(input())
command = input()
accumulated_profit = 0
is_profitable = False
while command != "Party!":
    cocktails = int(input())
    price = len(command) * cocktails
    if price % 2 == 1:
        price = 0.75 * price
    accumulated_profit += price
    if accumulated_profit >= expected_profit:
        is_profitable = True
        print(f'Target acquired.')
        break
    command = input()

if command == "Party!":
    print(f'We need {(expected_profit - accumulated_profit):.2f} leva more.')

print(f'Club income - {accumulated_profit:.2f} leva.')



