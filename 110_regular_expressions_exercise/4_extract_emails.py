import re


new_string = input()
regex = r'\b^[a-zA-Z0-9][0-9a-zA-Z-._]+@[\w\d][\w\d._-]+\.[\w]+\b'
emails = re.finditer(regex, new_string)

for email in emails:
    print(email.groups())