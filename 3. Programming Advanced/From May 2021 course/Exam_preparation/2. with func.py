def play_1(count: int, count_1: int, s_p1: int, seq, r: int, c: int):
    if not (0 <= r <= 6) and not (0 <= c <= 6):
        count += 1
        count_1 += 1

    elif seq[r][c] == "D":
        s_p1 -= (int(seq[r][0]) + int(seq[r][len(seq) - 1]) + int(seq[0][c]) + int(
            seq[len(seq) - 1][c])) * 2
    elif seq[r][c] == "T":
        s_p1 -= (int(seq[r][0]) + int(seq[r][len(seq) - 1]) + int(seq[0][c]) + int(
            seq[len(seq) - 1][c])) * 3
    elif seq[r][c] == "B":
        s_p1 = 0
    else:
        s_p1 -= int(seq[row][col])
    count += 1
    count_1 += 1
    return count, count_1, s_p1


def play_2(count, count_2, s_p2, seq, r, c):
    if not (0 <= r <= 6) and not (0 <= c <= 6):
        count += 1
        count_2 += 1

    elif seq[r][c] == "D":
        s_p2 -= (int(seq[r][0]) + int(seq[r][len(seq) - 1]) + int(seq[0][c]) + int(
            seq[len(seq) - 1][c])) * 2
    elif seq[r][c] == "T":
        s_p2 -= (int(seq[r][0]) + int(seq[r][len(seq) - 1]) + int(seq[0][c]) + int(
            seq[len(seq) - 1][c])) * 3
    elif seq[r][c] == "B":
        s_p2 = 0
    else:
        s_p2 -= int(seq[r][c])
    count += 1
    count_2 += 1
    return count, count_2, s_p2


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
        turn, turn_1, score_p1 = play_1(turn, turn_1, score_p1, matrix, row, col)
        continue

    elif turn % 2 == 0:
        turn, turn_2, score_p2 = play_2(turn, turn_2, score_p2, matrix, row, col)
        continue

if score_p1 <= 0:
    print(f'{player_1} won the game with {turn_1} throws!')
elif score_p2 <= 0:
    print(f'{player_2} won the game with {turn_2} throws!')
