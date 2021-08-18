command = input()
products_dict = {}
while not command == "buy":
    product_name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product_name not in products_dict:
        products_dict[product_name] = {}
        products_dict[product_name][price] = quantity
    else:
        old_quantity = products_dict[product_name]. copy()
        for key, value in products_dict[product_name].items():
            products_dict[product_name].pop(key)
            products_dict[product_name][price] = quantity + value
            break

    command = input()

for product_name in products_dict:
    for price, quantity in products_dict[product_name].items():
        print(f'{product_name} -> {(price * quantity):.2f}')
