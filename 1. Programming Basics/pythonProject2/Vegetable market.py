N = float(input())
M = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
profit_BGN = (vegetables_kg * N) + (fruits_kg * M)
profit_EUR = profit_BGN / 1.94
profit_EUR_format = "{:.2f}".format(profit_EUR)
print(profit_EUR_format)
