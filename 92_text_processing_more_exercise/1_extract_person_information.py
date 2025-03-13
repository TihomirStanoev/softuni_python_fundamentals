class Extractor:
    def __init__(self):
        self.name = ''
        self.age = 0

    def extract_name(self, string):
        name = ''

        is_found = False
        for i, letter in enumerate(string):
            if letter == '@':
                for index in range(i + 1, len(string)):
                    if string[index] == '|':
                        is_found = True
                        break
                    name += string[index]
            if is_found:
                break

        self.name = name

    def extract_ages(self, string):
        ages = ''

        is_found = False
        for i, letter in enumerate(string):
            if letter == '#':
                for index in range(i + 1, len(string)):
                    if string[index] == '*':
                        is_found = True
                        break
                    ages += string[index]
            if is_found:
                break

        self.age = int(ages)

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


extractor = Extractor()

string_counts = int(input())

for _ in range(string_counts):
    current_string = input()
    extractor.extract_name(current_string)
    extractor.extract_ages(current_string)
    print(extractor)
