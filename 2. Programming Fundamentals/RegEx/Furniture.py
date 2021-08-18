import re
furniture_list = []
total_cost_item = 0
text = input()
while not text == "Purchase":
    pattern = r"(?<=>>)(?P<Furniture>[A-Za-z]+)<<(?P<Price>[0-9]+[\.0-9]*)!(?P<Quantity>[0-9]+)"
    valid_info = re.finditer(pattern, text)
    for info in valid_info:
        current_info = info.groupdict()
        furniture_list.append(current_info['Furniture'])
        cost_item = float(current_info['Price']) * int(current_info['Quantity'])
        total_cost_item += cost_item
    text = input()

print(f"Bought furniture:")
for el in furniture_list:
    print(el)
print(f'Total money spend: {total_cost_item:.2f}')