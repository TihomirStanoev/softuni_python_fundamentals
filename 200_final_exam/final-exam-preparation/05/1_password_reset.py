class PasswordReset:
    def __init__(self, new_password):
        self._password = new_password

    @property
    def password(self):
        return self._password

    def take_odd(self):
        self._password = ''.join(char for index, char in enumerate(self._password) if index % 2 != 0)
        self.__str__()

    def cut(self, index, length):
        self._password = self._password[:index] + self._password[index + length:]
        self.__str__()

    def substitute(self, substring, substitute):
        if substring in self._password:
            self._password = self._password.replace(substring, substitute)
            self.__str__()
        else:
            print("Nothing to replace!")

    def __str__(self):
        print(self._password)


password_str = input()
user_password = PasswordReset(password_str)

while True:
    command = input()
    if command == 'Done':
        break

    command_list = command.split()
    action = command_list[0]

    if action == 'TakeOdd':
        user_password.take_odd()

    elif action == 'Cut':
        given_index, given_length = int(command_list[1]), int(command_list[2])
        user_password.cut(given_index, given_length)

    elif action == 'Substitute':
        given_substring, given_substitute =  command_list[1], command_list[2]
        user_password.substitute(given_substring, given_substitute)

print(f'Your password is: {user_password.password}')