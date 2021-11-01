def make_bold(ref_func):
    def wrapper(*args):
        result = ref_func(*args)
        return f"<b>{result}</b>"
    return wrapper


def make_italic(ref_func):
    def wrapper(*args):
        result = ref_func(*args)
        return f"<i>{result}</i>"
    return wrapper


def make_underline(ref_func):
    def wrapper(*args):
        result = ref_func(*args)
        return f"<u>{result}</u>"
    return wrapper




@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
