number_of_electron = int(input())
end_result = []
n = 1
while number_of_electron >= 2 * (n ** 2):
    end_result.append(2 * (n ** 2))
    number_of_electron -= 2 * (n ** 2)
    n += 1
if number_of_electron > 0:
    end_result.append(number_of_electron)
print(end_result)
