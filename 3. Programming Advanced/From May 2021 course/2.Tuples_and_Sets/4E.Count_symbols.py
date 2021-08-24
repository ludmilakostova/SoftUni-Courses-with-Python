expression = tuple(input())
result = {}
for el in expression:
    if el not in result:
        result[el] = 0
    result[el] += 1

sorted_result = sorted(result.items(), key=lambda x: x[0])
for key, value in sorted_result:
    print(f'{key}: {value} time/s')
