from collections import deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])
count = 0
while males and females:
    current_female = females[0]
    current_male = males[-1]

    if current_female <= 0:
        females.popleft()
        continue
    elif current_male <= 0:
        males.pop()
        continue

    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    elif current_male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if current_female == current_male:
        females.popleft()
        males.pop()
        count += 1
    else:
        females.popleft()
        males[-1] -= 2

reversed_males = []
for _ in range(len(males)):
    reversed_males.append(males.pop())

print(f'Matches: {count}')
if reversed_males:
    print(f'Males left: {", ".join([str(el) for el in reversed_males])}')
else:
    print("Males left: none")
if females:
    print(f'Females left: {", ".join([str(el) for el in females])}')
else:
    print("Females left: none")