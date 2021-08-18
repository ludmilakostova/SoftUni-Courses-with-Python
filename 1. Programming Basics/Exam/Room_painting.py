import math
painting_box = int(input())
wall_rolls = int(input())
gloves_price = float(input())
blush_price = float(input())
needed_gloves = math.ceil(0.35 * wall_rolls)
needed_blush = math.floor(0.48 * painting_box)
expenses = 21.50 * painting_box + 5.20 * wall_rolls + needed_gloves * gloves_price + needed_blush * blush_price
delivery = 1 / 15 * expenses
print(f'This delivery will cost {delivery:.2f} lv.')
