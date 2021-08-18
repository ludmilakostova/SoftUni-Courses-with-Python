number_cars = int(input())
cars = {}
while not number_cars == 0:
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    if not car in cars:
        cars[car] = {'mileage': mileage, 'fuel': fuel}
    number_cars -= 1

command = input()
while not command == "Stop":
    instruction = command.split(" : ")
    key_word = instruction[0]
    car = instruction[1]
    if key_word == "Drive":
        distance = int(instruction[2])
        fuel_needed = int(instruction[3])
        if cars[car]['fuel'] < fuel_needed:
            print(f'Not enough fuel to make that ride')
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100000:
            del cars[car]
            print(f'Time to sell the {car}!')
    elif key_word == "Refuel":
        new_fuel = int(instruction[2])
        cars[car]['fuel'] += new_fuel
        if cars[car]['fuel'] > 75:
            excess_fuel = cars[car]['fuel'] - 75
            refueled = new_fuel - excess_fuel
            cars[car]['fuel'] = 75
            print(f"{car} refueled with {refueled} liters")
        else:
            print(f"{car} refueled with {new_fuel} liters")

    elif key_word == "Revert":
        km = int(instruction[2])
        cars[car]['mileage'] -= km
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {km} kilometers')
    command = input()

sorted_cars = sorted(cars.items(), key=lambda tkvp: (-tkvp[1]['mileage'], tkvp[0]))
for car, data in sorted_cars:
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
