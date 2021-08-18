first_list = input().split(', ')
second_list = input().split(', ')
result = []
final_result = []
for el in first_list:
    for num in second_list:
        if el in num:
            result.append(el)
for el in result:
    if el not in final_result:
        final_result.append(el)
print(final_result)

# final_result = list(set(result))
# for i in range(len(final_result)):
#     if final_result[i] != first_list[i]:
#         final_result[i] = first_list[i]
