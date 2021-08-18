length = int(input())
width = int(input())
height = int(input())
water_excluded = float(input())
total = (length * width * height) / 1000
exclusion = water_excluded / 100
water = total * (1 - exclusion)
print(water)
