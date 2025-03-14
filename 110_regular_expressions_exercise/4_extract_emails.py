import re


class Email:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
        regex = r'\s([a-z0-9][a-z0-9\-\.\_]+[a-z0-9]@[a-z]+[a-z0-9\-]+[a-z](\.[a-z]+)+)'
        emails = re.finditer(regex, self.text)

        return '\n'.join(email.group(1) for email in emails)


single_string = input()

addresses = Email(single_string)

print(addresses.extract_emails())
