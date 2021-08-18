start_num = int(input())
end_num = int(input())
magic_num = int(input())
is_matched = False
total = 0
count = 0
for x in range(start_num, end_num + 1):
    for y in range(start_num, end_num + 1):
        total = x + y
        count += 1
        if total == magic_num:
            is_matched = True
            break
    if is_matched:
        break

if is_matched:
    print(f'Combination N:{count} ({x} + {y} = {magic_num})')
else:
    print(f'{count} combinations - neither equals {magic_num}')