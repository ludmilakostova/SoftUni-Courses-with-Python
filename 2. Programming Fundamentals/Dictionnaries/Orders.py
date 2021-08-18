command = input()
products_dict = {}
while not command == "buy":
    product_name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product_name not in products_dict:
        products_dict[product_name] = {}
    products_dict[product_name][price] = quantity

    command = input()

# for product_name in products_dict:
#     if len(products_dict[product_name]) == 1:
#         for price, quantity in products_dict[product_name].items():
#             print(f'{product_name} -> {price*quantity:.2f}')
#     else:
#         total_quantity = 0
#         for price, quantity in products_dict[product_name].items():
#             price = price
#             total_quantity += quantity
#         print(f'{product_name} -> {price*total_quantity:.2f}')
total_quantity = 0
for product_name in products_dict:
    total_quantity = 0
    for price in products_dict[product_name]:
        final_price = price
    for quantity in products_dict[product_name].values():
        total_quantity += quantity

    print(f'{product_name} -> {price*total_quantity:.2f}')


