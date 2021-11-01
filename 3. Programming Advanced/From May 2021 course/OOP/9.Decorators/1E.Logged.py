def logged(ref_func):
    def wrapper(*args):
        result = ""
        result += f"you called {ref_func.__name__}{args}\n"
        result += f"it returned {ref_func(*args)}"
        return result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

