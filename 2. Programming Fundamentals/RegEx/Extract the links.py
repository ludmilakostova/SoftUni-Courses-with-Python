import re
text = input()
pattern = r"(?P<Subdomain>w{3})\.(?P<DomainName>[A-Za-z0-9\-]+)(?P<DomainExtension>(\.[a-z]+)+)"
valid_url = []
while text != "":
    valid_links = re.finditer(pattern, text)

    for valid_link in valid_links:
        valid_url.append(valid_link.group())

    text = input()

for url in valid_url:
    print(url)
