class Repeats:
    def __init__(self):
        self.words = []

    def add_words(self, words):
        self.words = words.split()

    def __str__(self):
        return ''.join(word * len(word) for word in self.words)




repeat_string = Repeats()

new_string = input()
repeat_string.add_words(new_string)

print(repeat_string)

