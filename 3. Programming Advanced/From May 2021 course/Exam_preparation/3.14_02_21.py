def stock_availability(*args):
    inventory_list = args[0]
    if args[1] == "delivery":
        for i in range(2, len(args)):
            inventory_list.append(args[i])
    elif args[1] == "sell":
        if len(args) == 2:
            inventory_list.pop(0)

        elif isinstance(args[2], int):
            count = args[2]
            for i in range(len(inventory_list)):
                inventory_list.pop(0)
                count -= 1
                if count == 0:
                    break
        elif isinstance(args[2], str):
            for i in range(2, len(args)):
                while args[i] in inventory_list:
                    inventory_list.remove(args[i])

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
