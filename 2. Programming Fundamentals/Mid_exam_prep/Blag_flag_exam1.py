days_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
cumulated_plunder = 0
for i in range(1, days_plunder + 1):
    cumulated_plunder += daily_plunder
    if i % 3 == 0:
        cumulated_plunder += 0.5 * daily_plunder
    if i % 5 == 0:
        cumulated_plunder = 0.7 * cumulated_plunder
percentage = cumulated_plunder / expected_plunder * 100

if cumulated_plunder >= expected_plunder:
    print(f'Ahoy! {cumulated_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {percentage:.2f}% of the plunder.')