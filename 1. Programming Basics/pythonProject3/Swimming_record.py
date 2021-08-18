import math
record = float(input())
distance = float(input())
time_per_m = float(input())
time = distance * time_per_m
add_time = math.floor(distance / 15) * 12.5
total_time = time + add_time
if total_time < record:
    print(f' Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    needed_time = total_time - record
    print(f'No, he failed! He was {needed_time:.2f} seconds slower.')
