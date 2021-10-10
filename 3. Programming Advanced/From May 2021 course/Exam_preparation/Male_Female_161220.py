from collections import deque

males = [int(man) for man in input().split()]
females = deque([int(woman) for woman in input().split()])

matches_count = 0

while males and females:
    current_man = males[-1]
    current_woman = females[0]

    if current_woman <= 0:
        females.popleft()
        continue

    if current_man <= 0:
        males.pop()
        continue

    if current_woman == current_man:
        matches_count += 1
        males.pop()
        females.popleft()
    elif current_woman % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    elif current_man % 25 == 0:
        males.pop()
        if males:
            males.pop()
    else:
        females.popleft()
        males[-1] -= 2

reversed_males = reversed(males)
print(f'Matches: {matches_count}')
print(f'Males left: {", ".join(str(m) for m in reversed_males)}' if males else "Males left: none")
print(f'Females left: {", ".join(str(f) for f in females)}' if females else "Females left: none")

