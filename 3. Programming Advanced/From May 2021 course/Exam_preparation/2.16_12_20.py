expression = input()
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))
    if "P" in matrix[i]:
        curr_col = matrix[i].index("P")
        curr_rol = i

movements = int(input())
while movements > 0:
    command = input()
    position = (curr_rol, curr_col)
    if command == "up":
        new_row = curr_rol - 1
        new_col = curr_col
    elif command == "down":
        new_row = curr_rol + 1
        new_col = curr_col
    elif command == "right":
        new_row = curr_rol
        new_col = curr_col + 1
    elif command == "left":
        new_row = curr_rol
        new_col = curr_col - 1

    if (len(matrix) - 1 >= new_row >= 0) and (len(matrix) - 1 >= new_col >= 0):
        matrix[curr_rol][curr_col] = "-"
        if not (matrix[new_row][new_col] == "-"):
            expression += matrix[new_row][new_col]
        curr_rol, curr_col = new_row, new_col

    else:
        position = (curr_rol, curr_col)
        if len(expression) >= 1:
            expression = expression[:-1]

    matrix[curr_rol][curr_col] = "P"

    movements -= 1

print(expression)
for i in range(n):
    print("".join(matrix[i]))
