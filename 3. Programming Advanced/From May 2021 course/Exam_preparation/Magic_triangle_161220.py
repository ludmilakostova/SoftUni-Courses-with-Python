def is_in_range_row(r, size):
    if 0 <= r < size:
        return True
    return False


def is_in_range_col(c, size):
    if 0 <= c < size:
        return True
    return False


def get_magic_triangle(number):
    matrix = []
    for i in range(number):
        matrix.append([0] * (i + 1))

    for row in range(number):
        for col in range(len(matrix[row])):
            new_row = row - 1
            new_col_left = col - 1
            new_col_right = col

            if is_in_range_row(new_row, number) and is_in_range_col(new_col_left, len(matrix[row - 1])) and \
                    is_in_range_col(new_col_right, len(matrix[row - 1])):
                left = matrix[row - 1][col - 1]
                right = matrix[row - 1][col]
                matrix[row][col] = left + right
            else:
                matrix[row][col] = 1

    return matrix


print(get_magic_triangle(5))
