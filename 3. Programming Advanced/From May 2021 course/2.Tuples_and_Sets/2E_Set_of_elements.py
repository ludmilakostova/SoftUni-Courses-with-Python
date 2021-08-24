n, m = [int(el) for el in input().split()]

n_collection = set()
m_collection = set()
for _ in range(n):
    n_collection.add(input())

for _ in range(m):
    m_collection.add(input())
print(m_collection[2])

[print(el) for el in n_collection.intersection(m_collection)]

