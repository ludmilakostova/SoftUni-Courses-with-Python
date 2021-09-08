def get_magic_triangle(n):
    matrix = [1, [1, 1]]
    for i in range(n-2):
        matrix[i].append([])

    for i in range(2, len(matrix)):
        for j in range(i + 1):
            if j == 0 or j == i:
                matrix[i].append(matrix[i-1][i-1])
            else:
                matrix[i].append(matrix[i - 1][j-1] + matrix[i - 1][j])
    return print(matrix)


get_magic_triangle(5)
