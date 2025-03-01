class Synonyms:
    def __init__(self):
        self.count = 0
        self.synonyms_dict = dict()


    def get_words(self):

        for _ in range(self.count):
            key = input()
            value = input()

            if key not in self.synonyms_dict.keys():
                self.synonyms_dict[key] = value
            else:
                self.synonyms_dict[key] += f', {value}'


    def __str__(self):
        result = ''
        for key, value in self.synonyms_dict.items():
            result += f'{key} - {value}\n'

        return result


word = Synonyms()

word.count = int(input())
word.get_words()
print(word)
