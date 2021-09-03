player_1, player_2 = input().split(", ")
score_p1 = 501
score_p2 = 501
turn = 1
turn_1 = 0
turn_2 = 0
matrix = []
for i in range(7):
    matrix.append(input().split())


while not (score_p1 <= 0) and not (score_p2 <= 0):
    position = tuple(input())
    throw = []
    for el in position:
        if el.isdigit():
            throw.append(el)
    row, col = int(throw[0]), int(throw[1])

    if turn % 2 == 1:
        if not (0 <= row <= 6) and not (0 <= col <= 6):
            turn += 1
            turn_1 += 1
            continue
        elif matrix[row][col] == "D":
            score_p1 -= (int(matrix[row][0]) + int(matrix[row][len(matrix) - 1]) + int(matrix[0][col]) + int(
                matrix[len(matrix) - 1][col])) * 2
        elif matrix[row][col] == "T":
            score_p1 -= (int(matrix[row][0]) + int(matrix[row][len(matrix) - 1]) + int(matrix[0][col]) + int(
                matrix[len(matrix) - 1][col])) * 3
        elif matrix[row][col] == "B":
            score_p1 = 0
        else:
            score_p1 -= int(matrix[row][col])
        turn += 1
        turn_1 += 1
        continue

    elif turn % 2 == 0:
        if not (0 <= row <= 6) and not (0 <= col <= 6):
            turn += 1
            turn_2 += 1
            continue
        if matrix[row][col] == "D":
            score_p2 -= (int(matrix[row][0]) + int(matrix[row][len(matrix) - 1]) + int(matrix[0][col]) + int(
                matrix[len(matrix) - 1][col])) * 2
        elif matrix[row][col] == "T":
            score_p2 -= (int(matrix[row][0]) + int(matrix[row][len(matrix) - 1]) + int(matrix[0][col]) + int(
                matrix[len(matrix) - 1][col])) * 3
        elif matrix[row][col] == "B":
            score_p2 = 0
        else:
            score_p2 -= int(matrix[row][col])
        turn += 1
        turn_2 += 1
        continue

if score_p1 <= 0:
    print(f'{player_1} won the game with {turn_1} throws!')
elif score_p2 <= 0:
    print(f'{player_2} won the game with {turn_2} throws!')