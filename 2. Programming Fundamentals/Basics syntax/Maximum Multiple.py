import sys
divisor = int(input())
bound = int(input())
current_num = 0
max_num = -sys.maxsize
for num in range(divisor, bound + 1):
    if num % divisor == 0 and 0 < num <= bound:
        current_num = num
        if current_num > max_num:
            max_num = current_num
print(max_num)
