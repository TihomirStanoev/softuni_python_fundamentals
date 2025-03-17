import re


class Registration:
    def __init__(self,name):
        self.name = name

    def letters(self, case):
        if case == 'Lower':
            self.name = self.name.lower()
        elif case == 'Upper':
            self.name = self.name.upper()

        return self.name

    def reverse(self,start,end):
        name_range = range(0, len(self.name))
        if start in name_range and end in name_range:
            sub_string = self.name[start:end + 1]
            print(sub_string[::-1])

    def substring(self,substring):
        regex = fr'{substring}'

        matches = re.findall(regex, self.name)

        if matches:
            new_name = re.sub(regex,'',self.name)
            return new_name
        else:
            return f'The username {self.name} doesn\'t contain {substring}.'

    def replace_char(self,symbol):
        regex =fr'{symbol}'
        matches = re.findall(regex, self.name)
        if matches:
            self.name = re.sub(regex,'-',self.name)
            print(self.name)

    def is_valid(self,symbol):
        regex =fr'{symbol}'
        matches = re.findall(regex, self.name)
        if matches:
            return "Valid username."
        return f"{symbol} must be contained in your username."


username = input()
user = Registration(username)

while True:
    commands = input()
    if commands == 'Registration':
        break

    command = commands.split()

    if command[0] == 'Letters':
        print(user.letters(command[1]))

    elif command[0] == 'Reverse':
        user.reverse(int(command[1]), int(command[2]))

    elif command[0] == 'Substring':
        print(user.substring(command[1]))

    elif command[0] == 'Replace':
        user.replace_char(command[1])

    elif command[0] == 'IsValid':
        print(user.is_valid(command[1]))









