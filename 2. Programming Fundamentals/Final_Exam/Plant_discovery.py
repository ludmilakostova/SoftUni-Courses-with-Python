number_plants = int(input())
plants_collection = {}
while not number_plants == 0:
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant not in plants_collection:
        plants_collection[plant] = []
        plants_collection[plant].append(rarity)
    number_plants -= 1

command = input()

while not command == "Exhibition":
    instruction = command.split(": ")
    key_word = instruction[0]
    if key_word == "Rate":
        plant, rating = instruction[1].split(" - ")
        rating = int(rating)
        if plant in plants_collection:
            plants_collection[plant].append(rating)
        else:
            print("error")
    elif key_word == "Update":
        plant, new_rarity = instruction[1].split(" - ")
        new_rarity = int(new_rarity)
        if plant not in plants_collection:
            print("error")
        else:
            plants_collection[plant][0] = new_rarity
    elif key_word == "Reset":
        plant = instruction[1]
        plants_collection[plant] = [plants_collection[plant][0]]
    else:
        print(f'error')

    command = input()

for plant, value in plants_collection.items():
    if len(value) > 1:
        average_rating = sum(value[1:]) / len(value[1:])
        plants_collection[plant] = [value[0]]
        plants_collection[plant].append(average_rating)
    else:
        plants_collection[plant].append(0)

sorted_collection = sorted(plants_collection.items(), key=lambda x: (-x[1][0], -x[1][1]))
print(f'Plants for the exhibition:')
for plant, data in sorted_collection:
    print(f'- {plant}; Rarity: {data[0]}; Rating: {data[1]:.2f}')
