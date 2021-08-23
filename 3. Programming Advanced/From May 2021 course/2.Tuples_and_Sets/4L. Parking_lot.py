n = int(input())

cars = set()

for _ in range(n):
    command, plate = input().split(", ")
    if command == "IN":
        cars.add(plate)
    elif command == "OUT":
        if plate in cars:
            cars.remove(plate)

if not cars:
    print(f'Parking Lot is Empty')
else:
    [print(car) for car in cars]

