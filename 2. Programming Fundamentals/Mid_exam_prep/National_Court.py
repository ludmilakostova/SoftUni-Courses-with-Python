colleague_one = int(input())
colleague_two = int(input())
colleague_three = int(input())
total_count_people = int(input())
people_per_hour = colleague_one + colleague_two + colleague_three
hours = 0
while total_count_people > 0:
    hours += 1
    total_count_people -= people_per_hour
    if hours % 4 == 0:
        hours += 1
print(f'Time needed: {hours}h.')
