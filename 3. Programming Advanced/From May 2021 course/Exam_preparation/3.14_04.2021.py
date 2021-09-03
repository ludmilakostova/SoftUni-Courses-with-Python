def flights(*args, destination={}):
    for i in range(0, len(args), 2):
        if args[i] != "Finish":
            if args[i] not in destination:
                destination[args[i]] = args[i + 1]
            else:
                destination[args[i]] += args[i+1]
        else:
            return destination
            break


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
