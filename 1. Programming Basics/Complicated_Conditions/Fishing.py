budget = int(input())
season = input()
fishers_number = int(input())
rent = 0.0
if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishers_number <= 6:
    rent = 0.90 * rent
elif 6 < fishers_number <= 11:
    rent = 0.85 * rent
elif fishers_number >= 12:
    rent = 0.75 * rent

if fishers_number % 2 == 0:
    if season == "Summer" or season == "Spring" or season == "Winter":
        rent = 0.95 * rent

if rent <= budget:
    print(f'Yes! You have {(budget -  rent):.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(budget-rent):.2f} leva.')


