budget = float(input())
season = input()
place = ""
location = ""
if season == "summer":
    place = "Camp"
elif season == "winter":
    place = "Hotel"
if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        budget = 0.3 * budget
    elif season == "winter":
        budget = 0.70 * budget
elif 100 < budget <= 1000:
    location = "Balkans"
    if season == "summer":
        budget = 0.4 * budget
    elif season == "winter":
        budget = 0.80 * budget
elif budget > 1000:
    location = "Europe"
    budget = 0.9 * budget
    place = "Hotel"
print(f'Somewhere in {location}')
print(f'{place} - {budget:.2f}')

