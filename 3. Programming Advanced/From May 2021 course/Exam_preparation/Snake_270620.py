def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


N = int(input())
matrix = []
burrows_positions = []
for i in range(N):
    matrix.append(list(input()))
    for j in range(N):
        if matrix[i][j] == "S":
            position = (i, j)
        elif matrix[i][j] == "B":
            burrows_positions.append((i, j))

food_quantity = 0

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
row, col = position

while food_quantity < 10:
    direction = input()
    if direction in direction_mapper:
        new_row = row + direction_mapper[direction][0]
        new_col = col + direction_mapper[direction][1]
        matrix[row][col] = "."
        if is_in_range(new_row, new_col, N):
            if matrix[new_row][new_col] == "*":
                food_quantity += 1
                matrix[new_row][new_col] = "S"
            elif matrix[new_row][new_col] == "-":
                matrix[new_row][new_col] = "S"
            elif matrix[new_row][new_col] == "B":
                matrix[new_row][new_col] = "."
                burrows_positions.remove((new_row, new_col))
                new_row, new_col = burrows_positions[0][0], burrows_positions[0][-1]
                matrix[new_row][new_col] = "S"
            row, col = new_row, new_col
        else:
            break

print(f'You won! You fed the snake.' if food_quantity >= 10 else 'Game over!')
print(f'Food eaten: {food_quantity}')
for i in range(N):
    print("".join(matrix[i]))


