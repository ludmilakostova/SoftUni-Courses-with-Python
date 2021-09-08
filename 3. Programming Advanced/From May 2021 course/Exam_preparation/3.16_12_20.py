def get_magic_triangle(n: int, matrix=[1, [1, 1]], row=2):
    if len(matrix) == n:
        print(matrix)
        return

    matrix.append([])
    for j in range(row + 1):
        if j == 0 or j == row:
            matrix[row].append(matrix[row - 1][-1])
        else:
            matrix[row].append(matrix[row - 1][j - 1] + matrix[row - 1][j])
    get_magic_triangle(n, matrix, row + 1)


get_magic_triangle(5)
