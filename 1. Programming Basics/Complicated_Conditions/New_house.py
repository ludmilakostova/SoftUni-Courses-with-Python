flowers = input()
flowers_number = int(input())
budget = int(input())
price = 0.0
if flowers == "Roses":
    price = 5
elif flowers == "Dahlias":
    price = 3.80
elif flowers == "Tulips":
    price = 2.80
elif flowers == "Narcissus":
    price = 3
elif flowers == "Gladiolus":
    price = 2.50

spending = price * flowers_number

if flowers_number > 80 and flowers == "Roses":
    spending = 0.9 * spending
elif flowers_number > 90 and flowers == "Dahlias":
    spending = 0.85 * spending
elif flowers_number > 80 and flowers == "Tulips":
    spending = 0.85 * spending
elif flowers_number < 120 and flowers == "Narcissus":
    spending = 1.15 * spending
elif flowers_number < 80 and flowers == "Gladiolus":
    spending = 1.20 * spending

if spending > budget:
    print(f'Not enough money, you need {abs(spending - budget):.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {flowers_number} {flowers} and {abs(spending - budget):.2f} leva left.')