command = input()
my_list = command.split(' ')
new_list = []
for element in my_list:
    new_element = int(element)
    new_element = -1 * new_element
    new_list.append(new_element)
print(new_list)