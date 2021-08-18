tab_number = int(input())
salary = int(input())

for i in range(tab_number):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary < 0:
        break

if salary < 0:
    print(f'You have lost your salary.')
else:
    print(f'{salary}')
