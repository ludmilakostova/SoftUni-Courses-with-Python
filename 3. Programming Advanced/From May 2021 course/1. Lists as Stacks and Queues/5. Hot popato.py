from collections import deque


children = deque(input().split())
n = int(input())
while len(children) > 1:
    children.rotate(-n)
    print(f'Removed {children.pop}')

print(f'Last is {children.popleft()}')


