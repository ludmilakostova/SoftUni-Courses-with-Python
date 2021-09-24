from collections import deque

initial_seq = deque(input().split())

main_colors = {"red", "blue", "yellow"}
secondary_colors = {"orange", "purple", "green"}
collection = []

while initial_seq:
    left = initial_seq.popleft()
    right = initial_seq.pop() if initial_seq else ""

    color = left + right
    if color in main_colors or color in secondary_colors:
        collection.append(color)
        continue

    color = right + left
    if color in main_colors or color in secondary_colors:
        collection.append(color)
    else:
        left = left[:-1]
        right = right[:-1]
        if len(initial_seq) % 2 == 1:
            index = (len(initial_seq) // 2) + 1
        else:
            index = len(initial_seq) // 2
        if left:
            initial_seq.insert(index, left)
        if right:
            initial_seq.insert(index, right)

secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}
for color in collection:
    if color in main_colors:
        continue
    if secondary_colors[color][0] in collection and secondary_colors[color][1] in collection:
            pass
    else:
        collection.remove(color)

print(collection)
