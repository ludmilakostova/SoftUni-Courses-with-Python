n, m = [int(el) for el in input().split()]
snake = input()
matrix = []
for i in range(n):
    matrix.append([""] * m)

text_index = 0
col = 0
for row in range(n):
    if row % 2 == 0:
        dir = 1
    else:
        dir = -1

    while 0 <= col < m:
        matrix[row][col] = snake[text_index]
        if text_index + 1 == len(snake):
            text_index = 0
        else:
            text_index += 1
        col += dir

    col -= dir

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="")
    print()
