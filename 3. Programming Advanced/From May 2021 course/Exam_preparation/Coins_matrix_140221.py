def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


N = int(input())

matrix = []
for i in range(N):
    matrix.append(input().split())
    for j in range(N):
        if matrix[i][j] == "P":
            position = (i, j)

direction_mapper = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}
coins_count = 0
path = []
won = True

while coins_count <= 100:
    command = input()
    if command in direction_mapper:
        new_row = position[0] + direction_mapper[command][0]
        new_col = position[1] + direction_mapper[command][-1]
        if is_in_range(new_row, new_col, N):
            if matrix[new_row][new_col].isdigit():
                coins_count += int(matrix[new_row][new_col])
                path.append([new_row, new_col])
            elif matrix[new_row][new_col] == "X":
                coins_count //= 2
                won = False
                break
            position = (new_row, new_col)
        else:
            coins_count //= 2
            won = False
            break

if won:
    print(f'You won! You\'ve collected {coins_count} coins.')
else:
    print(f'Game over! You\'ve collected {coins_count} coins.')
print(f'Your path:')
for position in path:
    print(position)





