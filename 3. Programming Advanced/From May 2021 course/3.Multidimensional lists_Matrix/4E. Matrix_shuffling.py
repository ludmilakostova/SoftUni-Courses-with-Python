rows, cols = [int(el) for el in input().split()]
matrix = []

for i in range(rows):
    matrix.append([el for el in input().split()])

command = input()
while not command == "END":
    instruction = command.split()
    if not len(instruction) == 5:
        print("Invalid input!")
    else:
        key_word, row1, col1, row2, col2 = instruction[0], int(instruction[1]), int(instruction[2]), int(
            instruction[3]), int(instruction[4])
        if key_word == 'swap' and 0 <= row1 <= rows and 0 <= row2 <= rows and 0 <= col1 <= cols and 0 <= col2 <= cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for i in range(rows):
                for j in range(cols):
                    print(matrix[i][j], end=" ")
                print()
        else:
            print("Invalid input!")

    command = input()
