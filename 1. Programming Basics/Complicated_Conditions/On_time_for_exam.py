exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())
status = ""

total_exam_min = exam_hour * 60 + exam_min
total_arrival_min = arrival_hour * 60 + arrival_min
variation = total_arrival_min - total_exam_min

if variation > 0:
    status = "Late"
elif -30 <= variation <= 0:
    status = "On time"
elif variation < - 30:
    status = "Early"

print(f'{status}')

if - 60 < variation < 0:
    print(f'{abs(total_arrival_min - total_exam_min)} minutes before the start')
elif variation <= -60:
    variation_hour = abs(arrival_hour - exam_hour)
    variation_min = abs(arrival_min - exam_min)
    if variation_min < 10:
        print(f'{variation_hour}:0{variation_min} hours before the start')
    else:
        print(f'{variation_hour}:{variation_min} hours before the start')
elif 0 < variation < 60:
    print(f'{variation} minutes after the start')
elif variation > 60:
    variation_hour = arrival_hour - exam_hour
    variation_min = abs(arrival_min - exam_min)
    if variation_min < 10:
        print(f'{variation_hour}:0{variation_min} hours after the start')
    else:
        print(f'{variation_hour}:{variation_min} hours after the start')