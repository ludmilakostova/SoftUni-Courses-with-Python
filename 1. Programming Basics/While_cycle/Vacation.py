needed_money = float(input())
available_money = float(input())
count_days = 0
spending_days = 0
while available_money < needed_money and spending_days < 5:
    command = input()
    used_amount = float(input())
    count_days += 1
    if command == 'save':
        available_money += used_amount
        spending_days += 0
    elif command == 'spend':
        available_money -= used_amount
        spending_days += 1
        if available_money < 0:
            available_money = 0

if spending_days == 5:
    print(f'You can\'t save the money.')
    print(spending_days)
if available_money >= needed_money:
    print(f'You saved the money for {count_days} days.')