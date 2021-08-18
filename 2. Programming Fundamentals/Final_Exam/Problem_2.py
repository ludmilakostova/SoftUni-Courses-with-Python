import re
number_registration = int(input())
count = 0

while number_registration > 0:
     registration = input()
     pattern = r'(?P<surr>U\$)(?P<id>[A-Z][a-z]{2,})(?P=surr)(?P<surr_p>P@\$)(?P<password>[A-Za-z]{5,}\d+)(?P=surr_p)'
     matches = re.finditer(pattern, registration)
     validation = False
     for match in matches:
         count += 1
         current_match = match.groupdict()
         print(f'Registration was successful')
         print(f'Username: {current_match["id"]}, Password: {current_match["password"]}')
         validation = True
     if not validation:
        print(f'Invalid username or password')
     number_registration -= 1

print(f'Successful registrations: {count}')