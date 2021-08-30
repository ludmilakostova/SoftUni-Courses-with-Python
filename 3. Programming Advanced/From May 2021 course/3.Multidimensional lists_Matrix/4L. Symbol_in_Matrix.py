n = int(input())
matrix = []
for row in range(n):
    matrix.append([el for el in input()])

symbol_searched = input()
position = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol_searched:
            position = (row, col)
            break
    if position:
        break

if position:
    print(position)
else:
    print(f'{symbol_searched} does not occur in the matrix')


