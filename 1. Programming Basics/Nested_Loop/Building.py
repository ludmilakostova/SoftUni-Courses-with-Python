floor = int(input())
number = int(input())
for x in range(floor, 0, -1):
    for y in range(0, number):
        if x == floor:
            print(f'L{x}{y}', end=" ")
        elif x % 2 == 0:
            print(f'O{x}{y}', end=" ")
        else:
            print(f'A{x}{y}', end=" ")
    print()
