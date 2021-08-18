initial_sequence = input()
i = 0
while i < len(initial_sequence) -1:
    if initial_sequence[i] == initial_sequence[i+1]:
        initial_sequence = initial_sequence.replace(initial_sequence[i]*2, initial_sequence[i])
        i = 0
    else:
        i += 1

print(initial_sequence)