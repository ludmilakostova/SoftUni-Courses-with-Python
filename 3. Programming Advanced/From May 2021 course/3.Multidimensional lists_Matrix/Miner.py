def is_in_range(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


N = int(input())
directions = input().split()

matrix = []
total_coal = 0
for i in range(N):
    matrix.append(input().split())
    for j in range(N):
        if matrix[i][j] == "s":
            start_position = (i, j)
        elif matrix[i][j] == "c":
            total_coal += 1


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

row, col = start_position
count_coal = 0

for direction in directions:
    if direction in direction_mapper:
        new_row = row + direction_mapper[direction][0]
        new_col = col + direction_mapper[direction][1]
        if not is_in_range(new_row, new_col, N):
            position = (row, col)
        else:
            if matrix[new_row][new_col] == "*":
                pass
            elif matrix[new_row][new_col] == "c":
                count_coal += 1
                matrix[new_row][new_col] = "*"
                if count_coal == total_coal:
                    print(f'You collected all coal! ({new_row}, {new_col})')
                    exit(0)
            elif matrix[new_row][new_col] == "e":
                print(f'Game over! ({new_row}, {new_col})')
                exit(0)
            row, col = new_row, new_col

print(f'{total_coal - count_coal} pieces of coal left. ({row}, {col})')



