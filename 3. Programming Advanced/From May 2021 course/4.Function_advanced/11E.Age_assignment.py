def age_assignment(*args, res={}, **kwargs):
    for el in args:
        if el[0] in kwargs:
            res[el] = kwargs.get(el[0])
    return res


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

