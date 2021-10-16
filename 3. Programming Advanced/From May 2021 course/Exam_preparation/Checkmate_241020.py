def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


N = 8
matrix = []
for i in range(N):
    matrix.append(input().split())
    for j in range(N):
        if matrix[i][j] == "K":
            position = (i, j)

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "d_left_up": (-1, -1),
    "d_right_up": (-1, 1),
    "d_left_down": (1, -1),
    "d_right_down": (1, 1)
}
king_row, king_col = position
path = []

for direction in direction_mapper:
    new_row = king_row + direction_mapper[direction][0]
    new_col = king_col + direction_mapper[direction][1]
    while is_in_range(new_row, new_col, N):
        if matrix[new_row][new_col] == "Q":
            path.append([new_row, new_col])
            break
        row, col = new_row, new_col
        new_row = row + direction_mapper[direction][0]
        new_col = col + direction_mapper[direction][1]

if path:
    for el in path:
        print(el)
else:
    print("The king is safe!")






