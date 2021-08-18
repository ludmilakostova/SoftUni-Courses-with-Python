import sys
n = int(input())
max_number = -sys.maxsize
sum_number = 0
for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    sum_number += number

if sum_number - max_number == max_number:
    print(f'Yes')
    print(f'Sum = {max_number}')
else:
    print(f'No')
    print(f'Diff = {abs(max_number - sum_number + max_number)}')
