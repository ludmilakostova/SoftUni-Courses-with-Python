n = int(input())
count_2 = 0
count_3 = 0
count_4 = 0
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        count_2 += 1
    if number % 3 == 0:
        count_3 += 1
    if number % 4 == 0:
        count_4 += 1
p2 = count_2 / n * 100
p3 = count_3 / n * 100
p4 = count_4 / n * 100

print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')