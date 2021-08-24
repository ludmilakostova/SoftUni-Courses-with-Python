n = int(input())
sum_name = 0
set_even = set()
set_odd = set()
for i in range(1, n+1):
    name = input()
    for char in name:
        sum_name += ord(char)
    divided_number = int(sum_name/i)
    if divided_number % 2 == 0:
        set_even.add(divided_number)
    elif divided_number % 2 == 1:
        set_odd.add(divided_number)
    sum_name = 0

sum_even = sum(set_even)
sum_odd = sum(set_odd)

if sum_even == sum_odd:
    result = set_odd.union(set_even)
elif sum_even > sum_odd:
    result = set_odd.symmetric_difference(set_even)
elif sum_even < sum_odd:
    result = set_odd.difference(set_even)

print(", ".join([str(x) for x in result]))

