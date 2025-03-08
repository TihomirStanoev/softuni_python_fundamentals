class Reverse:
    def __init__(self):
        self.words = []

    def add_word(self, new_word):
        self.words.append(new_word)

    def __str__(self):
        return '\n'.join(f'{word} = {word[::-1]}' for word in self.words)


string = Reverse()

while True:
    command = input()
    if command == 'end':
        break

    string.add_word(command)

print(string)