def tags(symbol):
    def decorator(ref_func):
        def wrapper(*args):
            result = ""
            result += f"<{symbol}>{ref_func(*args)}</{symbol}>"
            return result
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

