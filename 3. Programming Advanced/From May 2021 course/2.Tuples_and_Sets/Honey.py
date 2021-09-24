from collections import deque

working_bees = deque([int(bee) for bee in input().split()])
nectar = [int(n) for n in input().split()]
symbols = deque(input().split())

honey_made = 0

while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar[-1]
    if current_nectar >= current_bee:
        current_symbol = symbols[0]
        if current_symbol == "+":
            honey_made += abs(current_bee + current_nectar)
        elif current_symbol == "/" and current_nectar > 0:
            honey_made += abs(current_bee / current_nectar)
        elif current_symbol == "-":
            honey_made += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            honey_made += abs(current_bee * current_nectar)
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()

print(f'Total honey made: {honey_made}')
if working_bees:
    print(f'Bees left: {", ".join([str(bee) for bee in working_bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(n) for n in nectar])}')
