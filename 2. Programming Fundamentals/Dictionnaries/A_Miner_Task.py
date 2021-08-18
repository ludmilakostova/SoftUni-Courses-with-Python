resource = input()
resources_dict = {}
while not resource == "stop":
    quantity = int(input())
    if resource not in resources_dict:
        resources_dict[resource] = quantity
    else:
        resources_dict[resource] += quantity
    resource = input()

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")