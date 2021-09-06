from math import log

num = int(input())
base = input()

if base == "natural":
    print(f'{log(num):.2f}')
else:
    print(log(num, int(base)))

