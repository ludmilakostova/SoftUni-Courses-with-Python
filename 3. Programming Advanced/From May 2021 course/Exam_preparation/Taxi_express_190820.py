from collections import deque

customers = deque([int(c) for c in input().split(", ")])
taxis = [int(t) for t in input().split(", ")]
time_driven = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]
    if current_customer <= current_taxi:
        time_driven += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {time_driven} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(c) for c in customers)}')
