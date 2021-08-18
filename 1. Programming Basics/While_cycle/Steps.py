count_steps = 0
while count_steps < 10000:
    next_command = input()
    if next_command == 'Going home':
        next_steps = int(input())
        count_steps += next_steps
        break
    next_steps = int(next_command)
    count_steps += next_steps

if count_steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{count_steps - 10000} steps over the goal!')
else:
    print(f'{10000 - count_steps} more steps to reach goal.')



