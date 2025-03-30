class ImitationGame:
    def __init__(self):
        self._message = ''

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message):
        self._message = new_message

    def move(self, number_of_letters):
        first_part = self._message[:number_of_letters]
        self._message = self._message[number_of_letters:] + first_part

    def insert(self, index, value):
        self._message = self._message[:index] + value + self._message[index:]

    def change_all(self, substring, replacement):
        while substring in self._message:
            self._message = self._message.replace(substring, replacement)

    def __str__(self):
        return f'The decrypted message is: {self.message}'



encrypted = ImitationGame()
encrypted.message = input()

commands_list = []


while True:
    command = input()
    if command == 'Decode':
        break
    commands_list.append(command)

for commands in commands_list:
    command = commands.split('|')
    function = command[0]

    if function == 'Move':
        letters = int(command[1])
        encrypted.move(letters)

    elif function == 'Insert':
        given_index = int(command[1])
        given_value = command[2]
        encrypted.insert(given_index, given_value)

    elif function == 'ChangeAll':
        given_substring = command[1]
        given_rep = command[2]
        encrypted.change_all(given_substring, given_rep)


print(encrypted)
