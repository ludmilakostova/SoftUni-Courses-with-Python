import math
income = float(input())
average_mark = float(input())
min_income = float(input())
subvention = 0
great_subvention = 0
if income > min_income and average_mark < 5.50:
    print(f'You cannot get a scholarship!')
elif income < min_income and 4.50 < average_mark:
    subvention = math.floor(0.35 * min_income)
if average_mark >= 5.50:
    great_subvention = math.floor(25 * average_mark)
    if subvention > great_subvention:
        print(f'You get a Social scholarship {subvention} BGN')
    else:
        print(f'You get a scholarship for excellent results {great_subvention} BGN')
