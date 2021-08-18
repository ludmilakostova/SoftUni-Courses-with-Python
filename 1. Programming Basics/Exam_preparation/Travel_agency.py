destination = input()
type_package = input()
VIP_discount = input()
days = int(input())
reservation_cost = 0
if days >= 1:
    if destination == "Bansko" or destination == "Borovets":
        if type_package == "withEquipment" and VIP_discount == "no":
            reservation_cost = 100 * days
        elif type_package == "withEquipment" and VIP_discount == "yes":
            reservation_cost = 0.90 * 100 * days
        elif type_package == "noEquipment" and VIP_discount == "no":
            reservation_cost = 80 * days
        elif type_package == "noEquipment" and VIP_discount == "yes":
            reservation_cost = 0.95 * 80 * days
        print(f'The price is {reservation_cost:.2f}lv! Have a nice time!')
    elif destination == "Burgas" or destination == "Varna":
        if type_package == "withBreakfast" and VIP_discount == "no":
            reservation_cost = 130 * days
        elif type_package == "withBreakfast" and VIP_discount == "yes":
            reservation_cost = 0.88 * 130 * days
        elif type_package == "noBreakfast" and VIP_discount == "no":
            reservation_cost = 100 * days
        elif type_package == "noBreakfast" and VIP_discount == "yes":
            reservation_cost = 0.93 * 100 * days
        print(f'The price is {reservation_cost:.2f}lv! Have a nice time!')
    else:
        print(f'Invalid input!')

else:
    print(f'Days must be positive number!')



