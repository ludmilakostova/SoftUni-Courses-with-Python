# Option 1
# print([round(float(el)) for el in input().split()])

# Option 2
nums = [float(el) for el in input().split()]
rounded = map(round, nums)
print(list(rounded))
