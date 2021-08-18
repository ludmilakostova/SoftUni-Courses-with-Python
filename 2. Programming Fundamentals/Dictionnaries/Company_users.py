command = input()
companies_dict = {}
while not command == 'End':
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies_dict:
        companies_dict[company_name] = []
    if employee_id not in companies_dict[company_name]:
        companies_dict[company_name].append(employee_id)

    command = input()

sorted_companies_dict = dict(sorted(companies_dict.items(), key=lambda x: x[0]))
for company_name, employee_id in sorted_companies_dict.items():
    print(f'{company_name}')
    for el in employee_id:
        print(f'-- {el}')
