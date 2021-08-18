sequence = [int(el) for el in input().split()]
command = input()
while command != "End":
    command_as_list = command.split()
    if command_as_list[0] == "Shoot":
        index = int(command_as_list[1])
        power = int(command_as_list[2])
        if 0 <= index < len(sequence):
            sequence[index] -= power
            if sequence[index] <= 0:
                sequence.remove(sequence[index])
    elif command_as_list[0] == "Add":
        index_add = int(command_as_list[1])
        value_added = int(command_as_list[2])
        if 0 <= index_add < len(sequence):
            sequence.insert(index_add, value_added)
        else:
            print(f'Invalid placement!')
    elif command_as_list[0] == "Strike":
        index_strike = int(command_as_list[1])
        radius = int(command_as_list[2])
        if 0 <= (index_strike - radius) <= len(sequence) and 0 <= (index_strike + radius) <= len(sequence):
            for i in range(index_strike - radius, index_strike + radius + 1):
                sequence.pop(index_strike - radius)
        else:
            print(f'Strike missed!')
    command = input()
sequence_as_string = [str(el) for el in sequence]
print('|'.join(sequence_as_string))
