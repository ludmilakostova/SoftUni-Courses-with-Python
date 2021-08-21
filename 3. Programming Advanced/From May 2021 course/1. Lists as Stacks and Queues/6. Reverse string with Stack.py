expression = input().split()
stack = []
while len(expression) > 0:
    stack.append(expression.pop())
print(" ".join(stack))
