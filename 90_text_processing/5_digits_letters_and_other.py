class Filter:
    def __init__(self, word):
        self.word = word

    def digit(self):
        return ''.join(digit for digit in self.word if digit.isnumeric())

    def letters(self):
        return ''.join(digit for digit in self.word if digit.isalpha())

    def others(self):
        return ''.join(digit for digit in self.word if not digit.isalnum())


word = input()
string = Filter(word)

print(string.digit())
print(string.letters())
print(string.others())
