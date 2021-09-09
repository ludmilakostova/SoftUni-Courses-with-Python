def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


matrix = []
n = 8
queens_positions = []

for i in range(n):
    matrix.append(input().split())

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

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "Q":
            for direction in directions:
                new_row = directions[direction][0] + row
                new_col = col + directions[direction][1]
                while is_in_range(new_row, new_col, n):
                    if matrix[new_row][new_col] == "Q":
                        break
                    if matrix[new_row][new_col] == "K":
                        queens_positions.append([row, col])
                        break
                    new_row += directions[direction][0]
                    new_col += directions[direction][1]

if queens_positions:
    for el in queens_positions:
        print(el)
else:
    print("The king is safe!")
