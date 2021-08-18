n1 = int(input())
n2 = int(input())
component = input()
result = 0
typ = ""
if component == '+':
    result = n1 + n2
elif component == "-":
    result = n1 - n2
elif component == "*":
    result = n1 * n2
elif component == "/":
    if n2 != 0:
        result = n1 / n2
        print(f'{n1} {component} {n2} = {result:.2f}')
    else:
        print(f"Cannot divide {n1} by zero")
elif component == "%":
    if n2 != 0:
        result = n1 % n2
        print(f'{n1} {component} {n2} = {result}')
    else:
        print(f"Cannot divide {n1} by zero")

if result % 2 == 0 and (component == "+" or component == "-" or component == "*"):
    typ = "even"
elif result % 2 == 1 and (component == "+" or component == "-" or component == "*"):
    typ = "odd"

if component == "+" or component == "-" or component == "*":
    print(f"{n1} {component} {n2} = {result} - {typ}")


