n_lines = int(input())
first_set = set()
second_set = set()
intersection = {}
for _ in range(n_lines):
    first_range, second_range = input().split("-")
    first_start, first_end = int(first_range.split(",")[0]), int(first_range.split(",")[1])
    second_start, second_end = int(second_range.split(",")[0]), int(second_range.split(",")[1])
    for i in range(first_start, first_end+1):
        first_set.add(i)
    for i in range(second_start, second_end+1):
        second_set.add(i)
    current_intersection = tuple(first_set.intersection(second_set))
    if current_intersection not in intersection:
        intersection[current_intersection] = len(current_intersection)
    first_set = set()
    second_set = set()

key_max = max(intersection.keys(), key= lambda x: intersection[x])
key_max =[int(el) for el in list(key_max)]
print(f'Longest intersection is {key_max} with length {len(key_max)}')





