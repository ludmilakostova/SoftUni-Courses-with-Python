rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - row - 1])
print(f'Primary diagonal: {", ".join(str(el) for el in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')
