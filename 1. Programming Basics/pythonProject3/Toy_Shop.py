travel_price = float(input())
puzzle_num = int(input())
kuk_num = int(input())
panda_num = int(input())
mimi_num = int(input())
truck_num = int(input())
profit = puzzle_num * 2.60 + kuk_num * 3 + panda_num * 4.10 + mimi_num * 8.20 + truck_num * 2
if (puzzle_num + kuk_num + panda_num + mimi_num + truck_num) < 50:
    gain_money = profit
else:
    gain_money = 0.75 * profit
total_earn = 0.90 * gain_money
if total_earn >= travel_price:
    budget = total_earn - travel_price
    print(f'Yes! {budget:.2f} lv left.')
else:
    budget = abs(total_earn - travel_price)
    print(f'Not enough money! {budget:.2f} lv needed.')
