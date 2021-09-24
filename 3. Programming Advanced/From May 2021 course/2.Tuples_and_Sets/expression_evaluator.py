from collections import deque

initial_seq = input().split()
collection = deque()
result = 0

mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for el in initial_seq:
    if el in mapper:
        result = collection.popleft()
        while collection:
            number = collection.popleft()
            result = mapper[el](result, number)
        collection.append(result)
    else:
        collection.append(int(el))

print(collection.popleft())
