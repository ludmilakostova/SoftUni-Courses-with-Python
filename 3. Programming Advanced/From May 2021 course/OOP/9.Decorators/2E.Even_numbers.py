def even_parameters(ref_func):
    def wrapper(*args):
        parameters = []
        for el in args:
            if isinstance(el, int) and el % 2 == 0:
                parameters.append(el)
        if len(parameters) == len(args):
            return ref_func(*args)
        return "Please use only even numbers!"
    return wrapper



@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
