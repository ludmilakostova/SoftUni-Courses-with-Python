initial_command = [int(el) for el in input().split(", ")]
n = 10
while initial_command:
    group = [el for el in initial_command if el <= n]
    for el in group:
        initial_command.remove(el)
    print(f'Group of {n}\'s: {group}')
    n += 10
    group = []
