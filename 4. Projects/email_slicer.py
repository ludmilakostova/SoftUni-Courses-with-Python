email_id = input("Please enter your e-mail: ").strip()
while True:
    try:
        username, domain_name = email_id.split("@")
        break
    except ValueError:
        print("Your e-mail must contain @")
        email_id = input("Please enter a correct e-mail: ").strip()

while True:
    try:
        mail_server, domain = domain_name.split(".")
        break
    except ValueError:
        print("The domain must contain a dot")
        domain_name = input("Please enter a correct domain: ").strip()

print(f'The composition of your email is as follows:\n- Username: {username}\n- Mail server: {mail_server}\n'
      f'- Domain extension: .{domain}')






