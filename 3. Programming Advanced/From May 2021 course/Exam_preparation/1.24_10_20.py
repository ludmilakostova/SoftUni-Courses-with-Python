from collections import deque

jobs = [int(el) for el in input().split(", ")]
searched_index = int(input())

cycles = deque(sorted([(jobs[index], index) for index in range(len(jobs))]))

result = 0
while cycles:
    job, index = cycles.popleft()
    result += job
    if index == searched_index:
        print(result)
        break
