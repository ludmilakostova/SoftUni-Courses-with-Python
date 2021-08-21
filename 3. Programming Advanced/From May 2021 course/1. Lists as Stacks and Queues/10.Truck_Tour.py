from collections import deque
number_pumps = int(input())
pump_queue = deque()

for _ in range(number_pumps):
    gas_pumps = input().split()
    pump_queue.append([int(gas_pumps[0]), int(gas_pumps[1])])

for i in range(number_pumps):
    fuel_tank = 0
    gas_pump_travelled = 0
    for gas_pumps in pump_queue:
        fuel, distance_to_next = gas_pumps[0], gas_pumps[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next:
            break
        fuel_tank -= distance_to_next
        gas_pump_travelled += 1
    if gas_pump_travelled == len(pump_queue):
        print(i)
        break

    pump_queue.rotate(-1)



    
