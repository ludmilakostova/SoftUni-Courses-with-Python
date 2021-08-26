n, m = [int(el) for el in input().split(" ")]
matrix = []
max_sum = 0
current_sum = 0
for row in range(n):
    matrix.append([int(el) for el in input().split(" ")])

for row in range(n - 2):
    for col in range(m - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] \
                      + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] \
                      + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position
print(f'Sum = {max_sum}')
print(f'{matrix[row][col]} {matrix[row][col + 1]} {matrix[row][col + 2]}')
print(f'{matrix[row + 1][col]} {matrix[row + 1][col + 1]} {matrix[row + 1][col + 2]}')
print(f'{matrix[row + 2][col]} {matrix[row + 2][col + 1]} {matrix[row + 2][col + 2]}')
