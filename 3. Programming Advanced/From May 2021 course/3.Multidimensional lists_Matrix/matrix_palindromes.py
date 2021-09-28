row, col = [int(el) for el in input().split()]
matrix = []
for r in range(row):
    matrix.append([0]*col)

for r in range(row):
    for c in range(col):
        matrix[r][c] = f"{chr(r+97)}{chr(r+c+97)}{chr(r+97)}"

for _ in range(len(matrix)):
    print(" ".join(matrix[_]))