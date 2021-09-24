from collections import deque

materials = [int(mat) for mat in input().split()]
magic_level = deque([int(magie) for magie in input().split()])
present_crafted = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
is_done = False

while materials and magic_level:
    current_box = materials[-1]
    current_magie = magic_level[0]

    if current_box == 0 and current_magie == 0:
        materials.pop()
        magic_level.popleft()
        continue
    elif current_magie == 0:
        magic_level.popleft()
        continue
    elif current_box == 0:
        materials.pop()
        continue

    current_magic_level = current_box * current_magie
    if current_magic_level == 150:
        present_crafted["Doll"] += 1
    elif current_magic_level == 250:
        present_crafted["Wooden train"] += 1
    elif current_magic_level == 300:
        present_crafted["Teddy bear"] += 1
    elif current_magic_level == 400:
        present_crafted["Bicycle"] += 1
    if current_magic_level == 150 or current_magic_level == 250 or current_magic_level == 300 or current_magic_level == 400:
        materials.pop()
        magic_level.popleft()
        if (present_crafted["Doll"] >= 1 and present_crafted["Wooden train"] >= 1) or \
                (present_crafted["Teddy bear"] >= 1 and present_crafted["Bicycle"] >= 1):
            is_done = True
        continue

    if current_magic_level < 0:
        current_magic_level = current_box + current_magie
        materials.pop()
        magic_level.popleft()
        materials.append(current_magic_level)
    else:
        magic_level.popleft()
        materials[-1] += 15

if is_done:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(reversed([str(box) for box in materials]))}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')
sorted_collection = sorted(present_crafted.items(), key=lambda x: x[0])

for present, value in sorted_collection:
    if value > 0:
        print(f'{present}: {value}')
