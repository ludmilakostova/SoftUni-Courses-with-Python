colleague_one = int(input())
colleague_two = int(input())
colleague_three = int(input())
total_students = int(input())
questions_per_hour = colleague_one + colleague_two + colleague_three
allocated_time = 0
while total_students > 0:
    allocated_time += 1
    if allocated_time % 4 == 0:
        allocated_time += 1
    total_students -= questions_per_hour
print(f'Time needed: {allocated_time}h.')




