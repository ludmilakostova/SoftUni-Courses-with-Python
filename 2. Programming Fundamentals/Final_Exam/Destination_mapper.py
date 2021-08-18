import re

places = input()
places_map = []
pattern = r'(?P<surr>=|/)(?P<body>[A-Z][A-Za-z]{2,})(?P=surr)'

matches = re.finditer(pattern, places)
for match in matches:
    current_place = match.group("body")
    places_map.append(current_place)
total_length = 0
for place in places_map:
    total_length += len(place)

print(f'Destinations: {", ".join(places_map)}')
print(f'Travel Points: {total_length}')


