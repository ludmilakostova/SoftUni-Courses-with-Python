import math
typ = input()  # square, rectangle, circle или triangle):
area = 0
if typ == "square":
    a = float(input())
    area = a * a
elif typ == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif typ == "circle":
    r = float(input())
    area = math.pi * r ** 2
elif typ == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
print(f"{area:.3f}")

