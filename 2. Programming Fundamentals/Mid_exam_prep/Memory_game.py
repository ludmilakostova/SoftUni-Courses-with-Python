initial_sequence = [int(num) for num in input().split()]
command = input()
moves = 0
while not command == 'end':
    index_one, index_two = command.split()
    index_one = int(index_one)
    index_two = int(index_two)
    moves += 1
    if not 0 <= index_one < len(initial_sequence) or not 0 <= index_two < (
    len(initial_sequence)) or index_one == index_two:
        position = len(initial_sequence) // 2
        added_value = f'-{moves}a'
        initial_sequence.insert(position, added_value)
        initial_sequence.insert(position + 1, added_value)
        print(f'Invalid input! Adding additional elements to the board')

    if initial_sequence[index_two] == initial_sequence[index_one]:
        removed_element = initial_sequence[index_one]
        initial_sequence.pop(index_one)
        initial_sequence.pop(index_two)
        print(f'Congrats! You have found matching elements - {removed_element}!')
    else:
        print(f'Try again!')

    if len(initial_sequence) < 1:
        print(f'You have won in {moves} turns!')

    command = input()
initial_sequence_str = [str(num) for num in initial_sequence]
if len(initial_sequence) > 1:
    print(f'Sorry you lose :(\n{" ".join(initial_sequence_str)}')
