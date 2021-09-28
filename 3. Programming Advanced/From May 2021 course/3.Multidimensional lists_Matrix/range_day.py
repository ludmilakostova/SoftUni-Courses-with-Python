def new_move_position(instruction, r, c, count):
    if instruction == "up":
        return (r - count, c)
    elif instruction == "down":
        return (r + count, c)
    elif instruction == "right":
        return (r, c + count)
    elif instruction == "left":
        return (r, c - count)


def is_in_range(r, c, N):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


shoot_mapper = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

size_matrix = 5
matrix = []
targets_collection = []
for i in range(size_matrix):
    matrix.append(input().split())
    for j in range(size_matrix):
        if matrix[i][j] == "A":
            position = (i, j)
        elif matrix[i][j] == "x":
            targets_collection.append((i, j))

row, col = position
count_targets = len(targets_collection)
reached_targets = []
N = int(input())
won = False

for _ in range(N):
    command, *res = input().split()
    if command == "move":
        direction, steps = res
        steps = int(steps)
        new_row, new_col = new_move_position(direction, row, col, steps)
        if is_in_range(new_row, new_col, size_matrix):
            if (new_row, new_col) in targets_collection:
                pass
            elif matrix[new_row][new_col] == ".":
                row, col = new_row, new_col
                matrix[new_row][new_col] = "A"
        else:
            row, col = position

    elif command == "shoot":
        direction = res[0]
        if direction in shoot_mapper:
            new_row = row + shoot_mapper[direction][0]
            new_col = col + shoot_mapper[direction][1]
            while is_in_range(new_row, new_col, size_matrix):
                if matrix[new_row][new_col] == "x":
                    reached_targets.append([new_row, new_col])
                    matrix[new_row][new_col] = "."
                    if len(reached_targets) == count_targets:
                        won = True
                        break
                    break
                else:
                    row, col = new_row, new_col
                    new_row = row + shoot_mapper[direction][0]
                    new_col = col + shoot_mapper[direction][1]
            row, col = position
    if won:
        break


if won is True:
    print(f'Training completed! All {count_targets} targets hit.')
else:
    print(f'Training not completed! {count_targets - len(reached_targets)} targets left.')
for el in reached_targets:
    print(el)
