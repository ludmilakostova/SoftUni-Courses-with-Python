lines_number = int(input())
set_chemicals = set()
for _ in range(lines_number):
    command = input().split()
    for el in command:
        set_chemicals.add(el)
[print(el) for el in set_chemicals]

