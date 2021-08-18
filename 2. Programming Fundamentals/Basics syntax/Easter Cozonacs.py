budget = float(input())
flour_price = float(input())
current_bakery = 0
colored_eggs = 0
money_left = 0
eggs_price = 0.75 * flour_price
milk_price = (1.25 * flour_price)/4
price_bakery = flour_price + eggs_price + milk_price
remaining_budget = budget - price_bakery
while remaining_budget >= 0:
    current_bakery += 1
    if current_bakery % 1 == 0:
        colored_eggs += 3
    if current_bakery % 3 == 0:
        lost_eggs = current_bakery - 2
        colored_eggs -= lost_eggs
        if colored_eggs < 0:
            break
    remaining_budget -= price_bakery
print(f'You made {current_bakery} cozonacs! Now you have {colored_eggs} eggs and {remaining_budget + price_bakery:.2f}BGN left.')
