from errors import *


command = input()
allowed_domain = [".com", ".bg", ".org", ".net"]
while not command == "End":
    email = command
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain, *res = email.split("@")

    if len(res) > 0:
        raise TooManySymbolsAt("Too many @ symbols")

    if len(username) < 4:
        raise NameTooShortError("Name must be more than 4 characters")
    
    if "." + domain.split(".")[-1] not in allowed_domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print(f'Email is valid')
    command = input()

