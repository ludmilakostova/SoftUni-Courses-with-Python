bought_food = int(input())
command = input()
bought_food_gr = bought_food * 1000
while command != 'Adopted':
    command_in_gr = int(command)
    bought_food_gr -= command_in_gr
    command = input()

if bought_food_gr >= 0:
    print(f'Food is enough! Leftovers: {bought_food_gr} grams.')
else:
    print(f'Food is not enough. You need {abs(bought_food_gr)} grams more.')