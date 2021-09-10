from collections import deque

effects = deque([int(el) for el in input().split(", ")])
casings = [int(el) for el in input().split(", ")]

datura_count = 0
cherry_count = 0
smoke_count = 0
is_bomb_pouch = False

while effects and casings:
    curr_effect = effects[0]
    curr_casing = casings[-1]
    curr_effect_casing = curr_effect + curr_casing

    if curr_effect_casing == 40:
        datura_count += 1
    elif curr_effect_casing == 60:
        cherry_count += 1
    elif curr_effect_casing == 120:
        smoke_count += 1
    else:
        casings[-1] -= 5

    if curr_effect_casing == 40 or curr_effect_casing == 60 or curr_effect_casing == 120:
        effects.popleft()
        casings.pop()

    if datura_count >= 3 and cherry_count >= 3 and smoke_count >= 3:
        is_bomb_pouch = True
        break

if is_bomb_pouch:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f'You don\'t have enough materials to fill the bomb pouch.')

if effects:
    print(f'Bomb Effects: {", ".join([str(el) for el in effects])}')
else:
    print(f'Bomb Effects: empty')

if casings:
    print(f'Bomb Casings: {", ".join([str(el) for el in casings])}')
else:
    print(f'Bomb Casings: empty')

print(f'Cherry Bombs: {cherry_count}\nDatura Bombs: {datura_count}\nSmoke Decoy Bombs: {smoke_count}')
