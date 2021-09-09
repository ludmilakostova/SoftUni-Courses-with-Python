def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


matrix = []
n = 8

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == "K":
            king_position = (i, j)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1)
}
queen = []
for direction in directions:
    king_row, king_col = king_position
    new_row = king_row + directions[direction][0]
    new_col = king_col + directions[direction][1]
    while is_in_range(new_row, new_col, n):
        if matrix[new_row][new_col] == "Q":
            queen_position = [new_row, new_col]
            queen.append(queen_position)
            break
        new_row += directions[direction][0]
        new_col += directions[direction][1]

if queen:
    [print(position) for position in queen]
else:
    print("The king is safe!")

