command = input().split(', ')
count_of_beggars = int(input())
new_list_partial = []
final_list = []

for k in range(len(command)):
    command[k] = int(command[k])

for j in range(count_of_beggars):
    new_list_partial = command[j::count_of_beggars]
    final_list.append(sum(new_list_partial))

print(final_list)


