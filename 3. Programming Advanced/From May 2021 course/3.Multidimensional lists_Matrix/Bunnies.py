def is_in_range(r, c, n, m):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


def get_next_bunnies(bunnies, n, m):
    next_bunnies = []
    for r, c in bunnies:
        if is_in_range(r - 1, c, n, m):
            next_bunnies.append((r - 1, c))
        if is_in_range(r + 1, c, n, m):
            next_bunnies.append((r + 1, c))
        if is_in_range(r, c + 1, n, m):
            next_bunnies.append((r, c + 1))
        if is_in_range(r, c - 1, n, m):
            next_bunnies.append((r, c - 1))
    return next_bunnies


N, M = [int(el) for el in input().split()]
matrix = []

bunnies_position = []
for i in range(N):
    matrix.append(list(input()))
    for j in range(M):
        if matrix[i][j] == "P":
            position = (i, j)
        elif matrix[i][j] == "B":
            bunnies_position.append((i, j))

direction_mapper = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}

direction_command = list(input())
count_commands = 0
row, col = position
matrix[row][col] = "."
won = None
for direction in direction_command:
    if direction in direction_mapper:
        new_row = row + direction_mapper[direction][0]
        new_col = col + direction_mapper[direction][1]
        if not is_in_range(new_row, new_col, N, M):
            won = True
        elif matrix[new_row][new_col] == "B":
            won = False

        if not won:
            row, col = new_row, new_col

    next_bunnies = get_next_bunnies(bunnies_position, N, M)
    for r, c in next_bunnies:
        if r == row and c == col and not won:
            won = False
        matrix[r][c] = "B"
    bunnies_position += next_bunnies

    if won is not None:
        break

if won:
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end="")
        print()
    print(f'won: {row} {col}')

else:
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end="")
        print()
    print(f'dead: {row} {col}')
