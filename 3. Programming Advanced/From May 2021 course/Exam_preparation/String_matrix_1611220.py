def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


sequence = input()

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(input()))
    for j in range(N):
        if matrix[i][j] == "P":
            position = (i, j)

row, col = position

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

M = int(input())
for t in range(M):
    command = input()
    if command in direction_mapper:
        new_row = row + direction_mapper[command][0]
        new_col = col + direction_mapper[command][1]
        if is_in_range(new_row, new_col, N):
            if matrix[new_row][new_col] == "-":
                pass
            else:
                sequence += matrix[new_row][new_col]
            matrix[new_row][new_col] = "P"
            matrix[row][col] = "-"
            row, col = new_row, new_col
        else:
            if len(sequence) > 0:
                sequence = sequence[:-1]

print(sequence)
for _ in range(N):
    print("".join(matrix[_]))

