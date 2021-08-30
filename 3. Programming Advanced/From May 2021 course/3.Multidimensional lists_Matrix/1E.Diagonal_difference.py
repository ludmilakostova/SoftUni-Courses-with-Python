n = int(input())
matrix = []
primary_diagonal = 0
secondary_diagonal = 0
for row in range(n):
    matrix.append([int(el) for el in input().split()])
    primary_diagonal += matrix[row][row]
    secondary_diagonal += matrix[row][n - row - 1]
result = abs(primary_diagonal - secondary_diagonal)
print(result)




