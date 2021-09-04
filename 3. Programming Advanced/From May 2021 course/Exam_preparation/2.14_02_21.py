n = int(input())
matrix = []
for i in range(n):
    matrix.append(input().split())
    if "P" in matrix[i]:
        row = i
        col = matrix[i].index("P")
        position = (row, col)

score = 0
path = []
is_winning = True
while score < 100:
    command = input()
    current_row, current_col = position

    if command == "up":
        current_row -= 1
    elif command == "down":
        current_row += 1
    elif command == "left":
        current_col -= 1
    elif command == "right":
        current_col += 1
    else:
        continue

    position = (current_row, current_col)
    if (len(matrix) - 1) < current_row or current_row < 0 or (len(matrix) - 1) < current_col or current_col < 0 or matrix[current_row][current_col] == "X":
        score = int(score // 2)
        is_winning = False
        break
    else:
        score += int(matrix[current_row][current_col])
    path.append(position)

if is_winning:
    print(f'You won! You\'ve collected {score} coins.')
else:
    print(f'Game over! You\'ve collected {score} coins.')

print(f'Your path: ')
for i in range(len(path)):
    print(f'[{path[i][0]}, {path[i][1]}]')
