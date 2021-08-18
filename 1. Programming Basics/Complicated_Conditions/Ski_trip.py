period = int(input())
room_type = input()
mark = input()
price = 0
if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    if period < 10:
        price = 0.7 * 25
    elif 10 <= period < 15:
        price = 0.65 * 25
    elif period >= 15:
        price = 0.5 * 25
elif room_type == "president apartment":
    if period < 10:
        price = 0.9 * 35
    elif 10 <= period < 15:
        price = 0.85 * 35
    elif period >= 15:
        price = 0.8 * 35

if mark == "positive":
    price = price * 1.25
elif mark == "negative":
    price = 0.9 * price

print(f'{price * (period - 1):.2f}')