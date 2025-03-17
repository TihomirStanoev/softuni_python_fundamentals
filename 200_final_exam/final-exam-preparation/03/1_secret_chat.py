import re


class Chat:
    def __init__(self, message):
        self.message = message

    def insert_space(self, index):
        message_list = list(self.message)
        message_list.insert(index, ' ')
        self.message = ''.join(message_list)
        return self.message

    def reverse(self, substr):
        regex = fr'{substr}'
        sub_matches = re.search(regex, self.message)

        if sub_matches:
            start_index, end_index = sub_matches.span()[0], sub_matches.span()[1]

            message_start = self.message[:start_index]
            message_mid = self.message[start_index:end_index]
            message_end = self.message[end_index:]
            self.message = message_start + message_mid[::-1] + message_end

            return self.message
        return 'error'

    def change_all(self, substr, repl):
        regex = rf'{substr}'
        self.message = re.sub(regex, repl, self.message)
        return self.message

    def __str__(self):
        return f'You have a new text message: {self.message}'


concealed_message = input()
secret_chat = Chat(concealed_message)

while True:
    command = input()
    if command == 'Reveal':
        print(secret_chat)
        break

    splitted_command = command.split(':|:')
    function = splitted_command[0]

    if function == 'InsertSpace':
        index = int(splitted_command[1])
        print(secret_chat.insert_space(index))

    elif function == 'Reverse':
        substring = splitted_command[1]
        print(secret_chat.reverse(substring))

    elif function == 'ChangeAll':
        substring = splitted_command[1]
        replacement = splitted_command[2]
        print(secret_chat.change_all(substring, replacement))
