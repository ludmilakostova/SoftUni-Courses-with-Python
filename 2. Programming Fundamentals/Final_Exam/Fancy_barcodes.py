import re

count_barcodes = int(input())
product_group = ''

while not count_barcodes == 0:
    barcode = input()
    pattern = r"(?P<surr>@#+)(?P<body>[A-Z][A-Za-z0-9]{4,}[A-Z])(?P=surr)"

    matches = re.finditer(pattern, barcode)
    found = False
    for match in matches:
        current_match = match.group()
        for i in range(len(current_match)):
            if current_match[i].isdigit():
                product_group += current_match[i]

        if product_group == "":
            product_group = '00'
        print(f'Product group: {product_group}')
        product_group = ""
        found = True

    if not found:
        print(f'Invalid barcode')

    count_barcodes -= 1
