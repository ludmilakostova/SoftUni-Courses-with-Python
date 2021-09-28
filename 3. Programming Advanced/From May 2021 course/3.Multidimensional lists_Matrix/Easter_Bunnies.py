def is_in_range(r, c, M):
    if 0 <= r < M and 0 <= c < M:
        return True
    return False


N = int(input())
matrix = []
for i in range(N):
    matrix.append(input().split())
    for j in range(len(matrix[i])):
        if matrix[i][j] == "B":
            bunnie_position = (i, j)

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
eggs_collected_per_direction = {}
eggs_path = {}

for direction in direction_mapper:
    new_row = bunnie_position[0] + direction_mapper[direction][0]
    new_col = bunnie_position[1] + direction_mapper[direction][1]
    while is_in_range(new_row, new_col, N) and matrix[new_row][new_col] != "X":
        if direction not in eggs_collected_per_direction:
            eggs_collected_per_direction[direction] = int(matrix[new_row][new_col])
        else:
            eggs_collected_per_direction[direction] += int(matrix[new_row][new_col])
        if direction not in eggs_path:
            eggs_path[direction] = []
        eggs_path[direction].append([new_row, new_col])

        row, col = new_row, new_col
        new_row = row + direction_mapper[direction][0]
        new_col = col + direction_mapper[direction][1]

sorted_eggs_collected = sorted(eggs_collected_per_direction.items(), key=lambda x: -x[1])
print(sorted_eggs_collected[0][0])
for value in eggs_path[sorted_eggs_collected[0][0]]:
    print(value)
print(sorted_eggs_collected[0][1])



