price_ratings = [int(prices) for prices in input().split(", ")]
entry_point = int(input())
left_side = price_ratings[0:entry_point]
right_side = price_ratings[entry_point+1:]
left_side_cheap = []
left_side_expensive = []
right_side_cheap = []
right_side_expensive = []
command = input()
if command == "cheap":
    for i in range(len(left_side)):
        if left_side[i] < price_ratings[entry_point]:
            left_side_cheap.append(left_side[i])
    for i in range(len(right_side)):
        if right_side[i] < price_ratings[entry_point]:
            right_side_cheap.append(right_side[i])
elif command == "expensive":
    for i in range(len(left_side)):
        if left_side[i] >= price_ratings[entry_point]:
            left_side_expensive.append(left_side[i])
    for i in range(len(right_side)):
        if right_side[i] >= price_ratings[entry_point]:
            right_side_expensive.append(right_side[i])

if command == "cheap":
    if sum(left_side_cheap) >= sum(right_side_cheap):
        print(f'Left - {sum(left_side_cheap)}')
    else:
        print(f'Right - {sum(right_side_cheap)}')
elif command == "expensive":
    if sum(left_side_expensive) >= sum(right_side_expensive):
        print(f'Left - {sum(left_side_expensive)}')
    else:
        print(f'Right - {sum(right_side_expensive)}')
