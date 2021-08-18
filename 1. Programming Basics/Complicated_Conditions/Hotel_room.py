month = input()
nights_number = int(input())
studio_price = 0.0
apartment_price = 0.0

if month == "May" or month == "October":
    apartment_price = 65 * nights_number
    studio_price = 50 * nights_number
    if 7 < nights_number <= 14:
        studio_price = 0.95 * studio_price
    elif nights_number > 14:
        studio_price = 0.7 * studio_price
        apartment_price = 0.9 * apartment_price
elif month == "June" or month == "September":
    studio_price = 75.20 * nights_number
    apartment_price = 68.70 * nights_number
    if nights_number > 14:
        studio_price = 0.80 * studio_price
        apartment_price = 0.9 * apartment_price
elif month == "July" or month == "August":
    studio_price = 76 * nights_number
    apartment_price = 77 * nights_number
    if nights_number > 14:
        apartment_price = 0.9 * apartment_price

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')

