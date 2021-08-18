degrees = int(input())
time_of_day = input()
outfit = 0
shoes = 0
if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon" or time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degrees <= 24:
    if time_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')

