from collections import deque

bomb_effects = deque([int(effect) for effect in input().split(", ")])
bomb_casings = [int(casing) for casing in input().split(", ")]

datura_count = 0
cherry_count = 0
smoke_count = 0

is_bomb_pouch = False

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    bomb_sum = current_effect + current_casing

    if bomb_sum == 40:
        datura_count += 1
    elif bomb_sum == 60:
        cherry_count += 1
    elif bomb_sum == 120:
        smoke_count += 1
    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing)
        bomb_casings[-1] -= 5

    if datura_count >= 3 and cherry_count >= 3 and smoke_count >= 3:
        is_bomb_pouch = True
        break

print(
    'Bene! You have successfully filled the bomb pouch!' if is_bomb_pouch else 'You don\'t have enough materials to '
                                                                               'fill the bomb pouch.')
if bomb_effects:
    print(f'Bomb Effects: {", ".join([str(effect) for effect in bomb_effects])}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(casing) for casing in bomb_casings])}')
else:
    print('Bomb Casings: empty')

print(f'Cherry Bombs: {cherry_count}\nDatura Bombs: {datura_count}\nSmoke Decoy Bombs: {smoke_count}')
