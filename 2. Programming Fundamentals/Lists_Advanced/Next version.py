current_version = [int(el) for el in input().split('.')]
if current_version[-1] < 9:
    current_version[-1] += 1
if current_version[-1] == 9:
    current_version[-1] = 0
    current_version[-2] += 1
    if current_version[-2] > 9:
        current_version[-2] = 0
        current_version[-3] += 1
print(*current_version, sep='.')
