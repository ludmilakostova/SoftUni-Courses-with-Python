def shopping_list(budget, result="", bought_items=0, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'
    else:
        for product, value in kwargs.items():
            total_price = value[0] * value[1]
            if budget >= total_price:
                budget -= total_price
                bought_items += 1
                result += f'You bought {product} for {total_price:.2f} leva.\n'
            else:
                pass

            if bought_items == 5:
                return result

        return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
