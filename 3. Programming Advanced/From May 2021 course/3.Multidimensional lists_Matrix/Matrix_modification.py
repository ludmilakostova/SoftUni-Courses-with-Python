def is_in_range(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


N = int(input())
matrix = []
for _ in range(N):
    matrix.append([int(el) for el in input().split()])

instruction = input()
while not instruction == "END":
    command, row, col, value = instruction.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if is_in_range(row, col, N):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print(f'Invalid coordinates')
    instruction = input()

for i in range(N):
    print(" ".join([str(el) for el in matrix[i]]))

