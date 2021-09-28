def is_in_range(r, c, M):
    if 0 <= r < M and 0 <= c < M:
        return True
    return False


total_presents = int(input())
N = int(input())
matrix = []
good_kids_count = 0
for i in range(N):
    matrix.append(input().split())
    for j in range(N):
        if matrix[i][j] == "S":
            position = (i, j)
        elif matrix[i][j] == "V":
            good_kids_count += 1

command = input()
row, col = position
total_nice_kids = good_kids_count


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

while not command == "Christmas morning":
    new_row = row + direction_mapper[command][0]
    new_col = col + direction_mapper[command][1]
    if not is_in_range(new_row, new_col,N):
        row, col = position
        command = input()
        continue
    else:
        if matrix[new_row][new_col] == "V":
            total_presents -= 1
            good_kids_count -= 1
            matrix[row][col] = "-"
            matrix[new_row][new_col] = "S"
            row, col = new_row, new_col

        elif matrix[new_row][new_col] == "X" or matrix[new_row][new_col] == "-":
            matrix[row][col] = "-"
            matrix[new_row][new_col] = "S"
            row, col = new_row, new_col

        elif matrix[new_row][new_col] == "C":
            matrix[new_row][new_col] = "S"
            for direction in direction_mapper:
                cell_row = new_row + direction_mapper[direction][0]
                cell_col = new_col + direction_mapper[direction][1]
                if is_in_range(cell_row, cell_col, N):
                    if matrix[cell_row][cell_col] == "V":
                        good_kids_count -= 1
                        total_presents -= 1
                    elif matrix[cell_row][cell_col] == "X":
                        total_presents -= 1
                    matrix[cell_row][cell_col] = "-"
                matrix[row][col] = "-"
                if total_presents == 0:
                    break
            row, col = new_row, new_col

    if total_presents == 0:
        break
    command = input()

if good_kids_count > 0 and total_presents == 0:
    print('Santa ran out of presents!')
for i in range(N):
    print(" ".join(matrix[i]))
if good_kids_count == 0:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {good_kids_count} nice kid/s.')