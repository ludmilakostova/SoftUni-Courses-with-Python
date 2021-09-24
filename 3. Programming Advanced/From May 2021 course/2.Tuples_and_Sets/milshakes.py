from collections import deque

chocolates = [int(choc) for choc in input().split(", ")]
milk = deque([int(milk) for milk in input().split(", ")])

count_milshakes = 0
is_milshake_ready = False

while chocolates and milk:
    current_choc = chocolates[-1]
    current_milk = milk[0]
    if current_milk <= 0 and current_choc <= 0:
        milk.popleft()
        chocolates.pop()
        continue
    elif current_choc <= 0:
        chocolates.pop()
        continue
    elif current_milk <= 0:
        milk.popleft()
        continue

    if current_milk == current_choc:
        count_milshakes += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolates[-1] -= 5

    if count_milshakes == 5:
        is_milshake_ready = True
        break

if is_milshake_ready:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join(str(choc) for choc in chocolates)}')
else:
    print('Chocolate: empty')

if milk:
    print(f'Milk: {", ".join(str(m) for m in milk)}')
else:
    print('Milk: empty')
