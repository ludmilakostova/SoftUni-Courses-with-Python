product = input()
type_product = 0
if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
    type_product = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    type_product = "vegetable"
else:
    type_product = "unknown"
print(f'{type_product}')
