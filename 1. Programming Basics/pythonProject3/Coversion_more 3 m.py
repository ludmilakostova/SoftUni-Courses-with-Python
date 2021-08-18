number = float(input())
converted_from = input()
converted_to = input()
conversion = f'{converted_from}:{converted_to}'
converted_number = 0
if conversion == "m:mm":
    converted_number = number * 1000
elif conversion == "m:cm":
    converted_number = number * 100
elif conversion == "cm:m":
    converted_number = number / 100
elif conversion == "cm:mm":
    converted_number = number * 10
elif conversion == "mm:m":
    converted_number = number / 1000
elif conversion == "mm:cm":
    converted_number = number / 10
print(f"{converted_number:.3f}")
