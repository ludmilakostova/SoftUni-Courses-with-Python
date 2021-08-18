import re

string = input()
calories_food = []
full_food = []

pattern = r'(?P<surr>\||#)(?P<itemname>[\sA-Za-z]+)(?P=surr)(?P<expiration>\d{2}/\d{2}/\d{2})(?P=surr)(?P<calories>\b[0-9]{1,4}[0]?\b)(?P=surr)'

matches = re.finditer(pattern, string)

for match in matches:
    current_match = match.groupdict()
    calories_food.append(current_match["calories"])
    full_food.append(current_match["itemname"])
    full_food.append(current_match["expiration"])
    full_food.append(current_match['calories'])

result = sum([int(el) for el in calories_food])
days_to_last = result // 2000
print(f'You have food to last you for: {days_to_last} days!')
for i in range(0, len(full_food), 3):
    print(
        f'Item: {full_food[i]}, Best before: {full_food[i+1]}, Nutrition: {full_food[i+2]}')
