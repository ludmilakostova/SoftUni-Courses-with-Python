destination = input()

while destination != "End":
    min_budget = float(input())
    total_savings = 0

    while total_savings < min_budget:
        savings = float(input())
        total_savings += savings
    print(f'Going to {destination}!')
    destination = input()
