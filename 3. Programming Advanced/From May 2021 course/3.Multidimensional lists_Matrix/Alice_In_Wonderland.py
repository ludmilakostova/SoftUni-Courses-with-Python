def is_in_range(r, c, M):
    if 0 <= r < M and 0 <= c < M:
        return True
    return False


N = int(input())
matrix = []
total_bags = 0

for i in range(N):
    matrix.append(input().split())
    for j in range(N):
        if matrix[i][j] == "A":
            alice_position = (i, j)

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
matrix[alice_position[0]][alice_position[1]] = "*"
row, col = alice_position
won = None

while True:
    command = input()
    if command in direction_mapper:
        new_row = row + direction_mapper[command][0]
        new_col = col + direction_mapper[command][1]
        if not is_in_range(new_row, new_col, N):
            won = False
            break
        elif matrix[new_row][new_col] == "R":
            won = False
            matrix[new_row][new_col] = "*"
            break
        else:
            if matrix[new_row][new_col].isdigit():
                total_bags += int(matrix[new_row][new_col])
                if total_bags >= 10:
                    won = True
            matrix[new_row][new_col] = "*"
            row, col = new_row, new_col

    if won is not None:
        break

if won is False:
    print(f'Alice didn\'t make it to the tea party.')
else:
    print(f'She did it! She went to the party.')
for i in range(N):
    print(" ".join(matrix[i]))




