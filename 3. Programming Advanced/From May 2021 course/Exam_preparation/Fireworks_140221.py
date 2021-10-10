from collections import deque

fireworks_effect = deque([int(el) for el in input().split(", ")])
explosive_power = [int(e) for e in input().split(", ")]

Palm_count = 0
Willow_count = 0
Crossette_count = 0

is_firework_done = False

while fireworks_effect and explosive_power:
    current_effect = fireworks_effect[0]
    current_explosive = explosive_power[-1]

    if current_effect <= 0:
        fireworks_effect.popleft()
        continue
    if current_explosive <= 0:
        explosive_power.pop()
        continue

    current_mix = current_effect + current_explosive
    if current_mix % 3 == 0 and not current_mix % 5 == 0:
        Palm_count += 1
        fireworks_effect.popleft()
        explosive_power.pop()
    elif current_mix % 5 == 0 and not current_mix % 3 == 0:
        Willow_count += 1
        fireworks_effect.popleft()
        explosive_power.pop()
    elif current_mix % 3 == 0 and current_mix % 5 == 0:
        Crossette_count += 1
        fireworks_effect.popleft()
        explosive_power.pop()
    else:
        fireworks_effect[0] -= 1
        fireworks_effect.append(fireworks_effect.popleft())

    if Palm_count >= 3 and Willow_count >= 3 and Crossette_count >= 3:
        is_firework_done = True
        break

if is_firework_done:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f'Firework Effects left: {", ".join([str(el) for el in fireworks_effect])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(el) for el in explosive_power])}')
print(f'Palm Fireworks: {Palm_count}\nWillow Fireworks: {Willow_count}\nCrossette Fireworks: {Crossette_count}')