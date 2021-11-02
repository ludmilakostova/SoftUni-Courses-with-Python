def type_check(type):
    def decorator(ref_func):
        def wrapper(*args):
            if isinstance(args[0], type):
                result = ref_func(*args)
            else:
                result = "Bad Type"
            return result
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
