fraise_lv = float(input())
banane_kg = float(input())
orange_kg = float(input())
malini_kg = float(input())
fraise_kg = float(input())
price_malini = 0.5 * fraise_lv
price_orange = 0.6 * price_malini
price_banani = 0.2 * price_malini
total = fraise_lv * fraise_kg + malini_kg * price_malini + orange_kg * price_orange + price_banani * banane_kg
print(total)