first_command = input()
collection_cities = {}
while not first_command == "Sail":
    city, population, gold = first_command.split("||")
    population = int(population)
    gold = int(gold)

    if city not in collection_cities:
        collection_cities[city] = {"population": population, "gold": gold}
    else:
        collection_cities[city]["population"] += population
        collection_cities[city]["gold"] += gold
    first_command = input()

event = input()

while not event == "End":
    event_list = event.split("=>")
    key_word = event_list[0]
    city = event_list[1]
    if key_word == "Plunder":
        people = int(event_list[2])
        gold_stolen = int(event_list[3])
        print(f'{city} plundered! {gold_stolen} gold stolen, {people} citizens killed.')

        collection_cities[city]["population"] -= people
        collection_cities[city]["gold"] -= gold_stolen

        if collection_cities[city]["population"] <= 0 or collection_cities[city]['gold'] <= 0:
            del collection_cities[city]
            print(f'{city} has been wiped off the map!')

    elif key_word == "Prosper":
        gold_gained = int(event_list[2])
        if gold_gained < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            collection_cities[city]['gold'] += gold_gained
            print(f"{gold_gained} gold added to the city treasury. {city} now has {collection_cities[city]['gold']} gold.")

    event = input()

if not collection_cities:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    sorted_collection = sorted(collection_cities.items(), key=lambda x: (-x[1]['gold'], x[0]))
    print(f'Ahoy, Captain! There are {len(sorted_collection)} wealthy settlements to go to:')
    for city, data in sorted_collection:
        print(f'{city} -> Population: {data["population"]} citizens, Gold: {data["gold"]} kg')

