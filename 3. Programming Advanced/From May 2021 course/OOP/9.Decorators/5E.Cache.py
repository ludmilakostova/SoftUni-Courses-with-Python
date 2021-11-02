def cache(func):
    log = {}

    def wrapper(parameter):
        if parameter not in log:
            log[parameter] = func(parameter)
            return log[parameter]
        else:
            return log[parameter]
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)

