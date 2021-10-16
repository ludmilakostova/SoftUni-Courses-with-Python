from collections import deque

jobs = [int(el) for el in input().split(", ")]
searched_job_index = int(input())

cycles = deque(sorted([(jobs[i], i) for i in range(len(jobs))]))

result = 0

while cycles:
    job, index = cycles.popleft()
    result += job
    if index == searched_job_index:
        print(result)
        break







