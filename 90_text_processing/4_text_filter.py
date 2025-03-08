class TextFilter:
    def __init__(self):
        self.word_ban = []

    def banned_words(self, words):
        self.word_ban = words.split(', ')

    def filter(self, text):

        for word in self.word_ban:
            while word in text:
                text = text.replace(word, '*' * len(word))

        return text

string = TextFilter()

ban = input()
text = input()

string.banned_words(ban)
print(string.filter(text))