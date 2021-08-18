width = int(input())
length = int(input())
cake_size = width * length
count_parts = 0
while cake_size - count_parts >= 1:
    command = input()
    if command == 'STOP':
        break
    next_parts = int(command)
    count_parts += next_parts

if cake_size - count_parts >= 1:
    print(f'{cake_size - count_parts} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_size - count_parts)} pieces more.')