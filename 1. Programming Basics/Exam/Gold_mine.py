location_number = int(input())
for i in range(location_number):
    average_expected_gold = float(input())
    days_number = int(input())
    accumulated_gold = 0
    for j in range(days_number):
        found_gold = float(input())
        accumulated_gold += found_gold
    average_accumulated_gold = accumulated_gold / days_number
    if average_accumulated_gold >= average_expected_gold:
        print(f'Good job! Average gold per day: {average_accumulated_gold:.2f}.')
    else:
        print(f'You need {(average_expected_gold - average_accumulated_gold):.2f} gold.')



