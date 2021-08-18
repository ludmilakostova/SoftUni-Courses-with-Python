sequence = [int(target) for target in input().split()]
command = input()
while not command == 'End':
    key_word, index, value = command.split()
    index = int(index)
    value = int(value)
    if key_word == "Shoot" and index < len(sequence):
        sequence[index] -= value
        if sequence[index] <= 0:
            sequence.pop(index)
    elif key_word == "Add":
        if index < len(sequence):
            sequence.insert(index, value)
        else:
            print(f'Invalid placement!')
    elif key_word == "Strike":
        left_range = index - value
        right_range = index + value
        if left_range >= 0 and right_range < len(sequence):
            for index in range(left_range, right_range + 1):
                sequence.pop(left_range)
        else:
            print(f'Strike missed!')
    command = input()

sequence = [str(target) for target in sequence]
print('|'.join(sequence))