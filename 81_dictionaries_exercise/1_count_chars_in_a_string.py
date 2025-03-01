class Chars:
    def __init__(self, char_string):
        self.char_string = char_string
        self.char_dict = dict()

    def dict_create(self):
        word = self.char_string.replace(' ', '')

        for char in word:
            if char not in self.char_dict.keys():
                self.char_dict[char] = 1
            else:
                self.char_dict[char] += 1

    def __repr__(self):
        return '\n'.join(f'{key} -> {value}' for key, value in self.char_dict.items())


new_word = input()

char_count = Chars(new_word)
char_count.dict_create()
print(char_count)
