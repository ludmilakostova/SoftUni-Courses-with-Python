from itertools import permutations

result = ["".join(combi) for combi in permutations(input())]
for combi in result:
    print(combi)




