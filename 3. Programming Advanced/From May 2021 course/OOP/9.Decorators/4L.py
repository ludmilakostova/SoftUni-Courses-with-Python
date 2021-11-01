def multiply(times):
    def decorator(ref_func):
        def wrapper(num):
            func_res = ref_func(num)
            return times * func_res

        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
