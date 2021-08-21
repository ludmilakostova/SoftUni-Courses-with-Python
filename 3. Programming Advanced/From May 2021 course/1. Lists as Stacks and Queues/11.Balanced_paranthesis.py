expression = input()
stack = []
balanced_expression = True
for paren in expression:
    if paren in "({[":
        stack.append(paren)
    elif paren in ")]}":
        if len(stack) == 0:
            balanced_expression = False
            break

        opening_paren = stack.pop()
        if opening_paren == "(" and paren == ")":
            continue
        elif opening_paren == "{" and paren == "}":
            continue
        elif opening_paren == "[" and paren == "]":
            continue
        else:
            balanced_expression = False
            break
if balanced_expression:
    print("YES")
else:
    print("NO")
