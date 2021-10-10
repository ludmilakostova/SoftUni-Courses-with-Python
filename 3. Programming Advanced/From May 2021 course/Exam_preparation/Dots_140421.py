def is_in_range(r, c, M):
    if 0 <= r < M and 0 <= c < M:
        return True
    return False


player_one, player_two = input().split(", ")
matrix = []
N = 7
for _ in range(N):
    matrix.append(input().split())

turns_mapper = {0: player_two, 1: player_one}
score_mapper = {player_one: 501, player_two: 501}

turns_count = 1

while score_mapper[player_one] > 0 and score_mapper[player_two] > 0:
    current_player = turns_mapper[turns_count % 2]

    command = input().split(", ")
    row = int(command[0][-1])
    col = int(command[1][0])

    if is_in_range(row, col, N):
        if matrix[row][col].isdigit():
            score_mapper[current_player] -= int(matrix[row][col])
        elif matrix[row][col] == "D":
            amount = 2 * (int(matrix[row][0]) + int(matrix[row][N - 1]) + int(matrix[0][col]) + int(matrix[N - 1][col]))
            score_mapper[current_player] -= amount
        elif matrix[row][col] == "T":
            amount = 3 * (int(matrix[row][0]) + int(matrix[row][N - 1]) + int(matrix[0][col]) + int(matrix[N - 1][col]))
            score_mapper[current_player] -= amount
        elif matrix[row][col] == "B":
            score_mapper[current_player] = 0
        turns_count += 1
    else:
        turns_count += 1
        continue

print(f'{current_player} won the game with {turns_count// 2} throws!')