import math
party_size = int(input())
days = int(input())
companions_number = party_size
total_coins = 0
for i in range(1, days + 1):
    total_coins += 50
    if i % 10 == 0:
        companions_number -= 2
    if i % 15 == 0:
        companions_number += 5
    total_coins -= 2 * companions_number
    if i % 3 == 0:
        total_coins -= 3 * companions_number
    if i % 5 == 0:
        total_coins += 20 * companions_number
        if i % 3 == 0:
            total_coins -= 2 * companions_number
coins_per_companion = math.floor(total_coins/companions_number)
print(f'{companions_number} companions received {coins_per_companion} coins each.')


