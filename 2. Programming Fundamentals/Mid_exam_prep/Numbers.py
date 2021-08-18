initial_sequence = [int(num) for num in input().split()]
average_num_sequence = sum(initial_sequence) / len(initial_sequence)
new_sequence = []
final_sequence = []
for i in range(len(initial_sequence)):
    if initial_sequence[i] > average_num_sequence:
        new_sequence.append(initial_sequence[i])

if len(new_sequence) == 0:
    print(f'No')
    exit()
else:
    new_sequence.sort(reverse=True)

if len(new_sequence) > 5:
    for i in range(5):
        final_sequence.append(new_sequence[i])
    final_sequence = [str(num) for num in final_sequence]
    print(' '.join(final_sequence))
else:
    new_sequence = [str(num) for num in new_sequence]
    print(' '.join(new_sequence))
