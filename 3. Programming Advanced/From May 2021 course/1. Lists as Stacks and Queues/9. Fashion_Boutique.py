box_clothes_stack = [int(cloth) for cloth in input().split()]
rack_capacity = int(input())
initial_rack_capacity = rack_capacity
count_rack = 1
while box_clothes_stack:
    current_item = box_clothes_stack.pop()
    if rack_capacity - current_item >= 0:
        rack_capacity -= current_item
    else:
        count_rack += 1
        rack_capacity = initial_rack_capacity
        rack_capacity -= current_item
print(count_rack)
