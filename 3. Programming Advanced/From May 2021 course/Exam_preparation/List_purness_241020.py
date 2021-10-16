from collections import deque


def best_list_pureness(*args, max_result=0):
    pureness_list = deque(args[0])
    K = args[1]

    for rotation in range(K + 1):
        result = sum([pureness_list[i] * i for i in range(len(pureness_list))])
        if result > max_result:
            max_result = result
            count = rotation
        pureness_list.rotate(1)

    return f'Best pureness {max_result} after {count} rotations'


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
