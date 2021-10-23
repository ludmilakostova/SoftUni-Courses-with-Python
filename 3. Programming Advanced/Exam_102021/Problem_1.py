from collections import deque

materials = [int(mat) for mat in input().split()]
magic_level = deque([int(magie) for magie in input().split()])

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond = 0
is_crafted = False

while materials and magic_level:
    current_material = materials[-1]
    current_magic_level = magic_level[0]
    current_mix = current_material + current_magic_level

    if current_mix < 100:
        if current_mix % 2 == 0:
            current_mix = 2 * current_material + 3 * current_magic_level
        else:
            current_mix = 2 * (current_material + current_magic_level)

    if current_mix > 499:
        current_mix /= 2
    if 100 <= current_mix <= 199:
        gemstone += 1
    elif 200 <= current_mix <= 299:
        porcelain_sculpture += 1
    elif 300 <= current_mix <= 399:
        gold += 1
    elif 400 <= current_mix <= 499:
        diamond += 1

    if (gemstone >= 1 and porcelain_sculpture >= 1) or (gold >= 1 and diamond >= 1):
        is_crafted = True

    materials.pop()
    magic_level.popleft()

print('The wedding presents are made!' if is_crafted else 'Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ".join([str(m) for m in materials])}')
if magic_level:
    print(f'Magic left: {", ".join([str(mag) for mag in magic_level])}')
if diamond > 0:
    print(f'Diamond Jewellery: {diamond}')
if gemstone > 0:
    print(f'Gemstone: {gemstone}')
if gold > 0:
    print(f'Gold: {gold}')
if porcelain_sculpture > 0:
    print(f'Porcelain Sculpture: {porcelain_sculpture}')
