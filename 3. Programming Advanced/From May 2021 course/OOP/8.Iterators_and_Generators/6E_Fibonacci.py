def fibonacci():
    fo = 0
    f1 = 1
    yield fo
    yield f1
    fn_1 = f1
    fn_2 = fo
    while True:
        fn = fn_1 + fn_2
        yield fn
        fn_2 = fn_1
        fn_1 = fn


generator = fibonacci()
for i in range(5):
    print(next(generator))
