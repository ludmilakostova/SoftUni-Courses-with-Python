# Option 1
# from itertools import combinations
#
# result = list(combinations(input().split(", "), int(input())))
# print(result)
#
# for x, y in result:
#     print(x, y, sep=

# Option 2 - Recursion
def combinations(seq, count, current_names=[]):
    if len(current_names) == count:
        print(", ".join(current_names))
        return

    for i in range(len(seq)):
        current_names.append(seq[0])
        combinations(seq[i + 1], count, current_names)
        current_names.pop()


names = input().split(", ")
n = int(input())
combinations(names, n)
