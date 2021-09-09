from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    data = {}

    for rotation in range(k+1):
        result = sum([(index*value) for index, value in enumerate(numbers)])
        if rotation not in data:
            data[rotation] = result
        numbers.rotate(1)

    sorted_data = sorted(data.items(), key=lambda x: -x[1])
    return f'Best pureness {sorted_data[0][1]} after {sorted_data[0][0]} rotations'




test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)



