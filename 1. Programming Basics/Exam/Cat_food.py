cats_total = int(input())
small_cats_counter = 0
big_cats_counter = 0
enormous_cats_counter = 0
total_food_gr = 0
for i in range(1, cats_total + 1):
    food_gr = float(input())
    if 100 <= food_gr < 200:
        small_cats_counter += 1
        total_food_gr += food_gr
    elif 200 <= food_gr < 300:
        big_cats_counter += 1
        total_food_gr += food_gr
    elif 300 <= food_gr < 400:
        enormous_cats_counter += 1
        total_food_gr += food_gr
food_expenses = total_food_gr / 1000 * 12.45
print(f'Group 1: {small_cats_counter} cats.')
print(f'Group 2: {big_cats_counter} cats.')
print(f'Group 3: {enormous_cats_counter} cats.')
print(f'Price for food per day: {food_expenses:.2f} lv.')



