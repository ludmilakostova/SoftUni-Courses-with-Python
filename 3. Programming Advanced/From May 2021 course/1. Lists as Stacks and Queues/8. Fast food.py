from collections import deque

food_quantity_total = int(input())
orders_queue = deque()
for order in input().split():
    orders_queue.append(int(order))

max_order = max(orders_queue)


while orders_queue:
    current_order = orders_queue.popleft()
    if food_quantity_total - current_order >= 0:

        food_quantity_total -= current_order
    else:
        orders_queue.appendleft(current_order)
        break
print(max_order)
if len(orders_queue) == 0:
    print(f'Orders complete')
else:
    print(f'Orders left: {" ".join([str(order) for order in orders_queue])}')
