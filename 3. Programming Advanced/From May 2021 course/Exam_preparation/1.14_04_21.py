from collections import deque

pizza_orders = deque([int(el) for el in input().split(", ")])
capacity_employees = [int(el) for el in input().split(", ")]
count_total_pizzas = 0

while pizza_orders and capacity_employees:
    current_order = pizza_orders.popleft()
    while not (0 < current_order <= 10) and pizza_orders:
        current_order = pizza_orders.popleft()

    if 0 < current_order <= 10:
        current_capacity = capacity_employees.pop()
        if current_order <= current_capacity:
            count_total_pizzas += current_order
        else:
            count_total_pizzas += current_capacity
            remaining_order = current_order - current_capacity
            pizza_orders.appendleft(remaining_order)

remaining_employees = [str(el) for el in capacity_employees]
remaining_orders = [str(el) for el in pizza_orders]

if not pizza_orders:
    print(f'All orders are successfully completed!\nTotal pizzas made: {count_total_pizzas}')
    print(f'Employees: {", ".join(remaining_employees)}')
else:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join(remaining_orders)}')