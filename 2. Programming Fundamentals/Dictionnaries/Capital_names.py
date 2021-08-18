country_names = input().split(", ")
capital_names = input().split(", ")
country_capital_dict = dict(zip(country_names, capital_names))
for country_names, capital_names in country_capital_dict.items():
    print(f'{country_names} -> {capital_names} ')
