from collections import deque

firework_effect = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]

count_palm = 0
count_willow = 0
count_crossette = 0

enough_fireworks = False

while firework_effect and explosive_power:
    current_effect = firework_effect[0]
    current_power = explosive_power[-1]
    if current_effect <= 0:
        firework_effect.popleft()
        continue
    if current_power <= 0:
        explosive_power.pop()
        continue

    current_mix = current_effect + current_power
    if current_mix % 3 == 0 and not (current_mix % 5 == 0):
        count_palm += 1
        explosive_power.pop()
        firework_effect.popleft()
    elif current_mix % 5 == 0 and not (current_mix % 3 == 0):
        count_willow += 1
        explosive_power.pop()
        firework_effect.popleft()
    elif current_mix % 3 == 0 and current_mix % 5 == 0:
        count_crossette += 1
        explosive_power.pop()
        firework_effect.popleft()
    else:
        current_effect -= 1
        firework_effect[0] = current_effect
        firework_effect.rotate(-1)

    if count_willow >= 3 and count_palm >= 3 and count_crossette >= 3:
        enough_fireworks = True
        break

if enough_fireworks:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f'Sorry. You can\'t make the perfect firework show.')
if firework_effect:
    print(f'Firework Effects left: {", ".join([str(el) for el in firework_effect])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(el) for el in explosive_power])}')

print(f'Palm Fireworks: {count_palm}\nWillow Fireworks: {count_willow}\nCrossette Fireworks: {count_crossette}')
