def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


N = int(input())
bombs_number = int(input())

matrix = []
for i in range(N):
    matrix.append([0]*N)

for _ in range(bombs_number):
    row, col = input()[1:-1].split(", ")
    matrix[int(row)][int(col)] = "*"

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

for i in range(N):
    for j in range(N):
        if not matrix[i][j] == "*":
            for direction in direction_mapper:
                new_row = i + direction_mapper[direction][0]
                new_col = j + direction_mapper[direction][1]
                if is_in_range(new_row, new_col, N) and matrix[new_row][new_col] == "*":
                    matrix[i][j] += 1
for i in range(N):
    print(" ".join([str(el) for el in matrix[i]]))
