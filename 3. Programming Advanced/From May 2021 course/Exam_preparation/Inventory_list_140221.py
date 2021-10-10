from collections import deque


def stock_availability(items: list, command: str, *args):
    items = deque(items)
    if command == "delivery":
        for el in args:
            items.append(el)
    elif command == "sell":
        if not args:
            items.popleft()
            return list(items)
        for i in range(len(args)):
            if isinstance(args[i], int):
                for j in range(int(args[i])):
                    items.popleft()
            elif isinstance(args[i], str):
                while args[i] in items:
                    items.remove(args[i])
    return list(items)



print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


