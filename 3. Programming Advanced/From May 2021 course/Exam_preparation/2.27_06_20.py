def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


in_range = True

n = int(input())
matrix = []
burrows = []
for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == "S":
            snake_position = (i, j)
        elif matrix[i][j] == "B":
            burrows.append((i, j))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

snake_row, snake_col = snake_position
food_quantity = 0
while True:
    command = input()
    if command in directions:
        new_rol = snake_row + directions[command][0]
        new_col = snake_col + directions[command][1]

        matrix[snake_row][snake_col] = "."

        if is_in_range(new_rol, new_col, n):
            if matrix[new_rol][new_col] == "*":
                food_quantity += 1
                snake_row, snake_col = new_rol, new_col
                matrix[snake_row][snake_col] = "S"
                if food_quantity >= 10:
                    break
            elif matrix[new_rol][new_col] == "B":
                matrix[new_rol][new_col] = "."
                snake_row, snake_col = burrows[-1]
                matrix[snake_row][snake_col] = "S"
            elif matrix[new_rol][new_col] == "-":
                snake_row, snake_col = new_rol, new_col
                matrix[snake_row][snake_col] = "S"
        else:
            in_range = False
            break

if in_range:
    print(f'You won! You fed the snake.')
else:
    print(f'Game over!')

print(f'Food eaten: {food_quantity}')

for _ in range(n):
    print("".join(matrix[_]))
