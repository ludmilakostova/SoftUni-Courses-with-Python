lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expense = 0
broken_shield = 0
for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        total_expense += helmet_price
    if i % 3 == 0:
        total_expense += sword_price
    if i % 2 == 0 and i % 3 == 0:
        total_expense += shield_price
        broken_shield += 1
        if broken_shield % 2 == 0:
            total_expense += armor_price
print(f'Gladiator expenses: {total_expense:.2f} aureus')