import math
person_num = int(input())
capacity_lift = int(input())
if capacity_lift >= person_num:
    elevation = 1
else:
    elevation = math.ceil(person_num/capacity_lift)
print(elevation)