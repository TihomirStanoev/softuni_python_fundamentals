class OddOccurrences:
    string_of_elements = []
    language = {}

    @classmethod
    def get_input(cls):
        cls.string_of_elements = input().split()
        cls.string_of_elements = list(map(lambda x: x.lower(), cls.string_of_elements))
        cls.get_languages()

    @classmethod
    def get_languages(cls):
        for itm in cls.string_of_elements:
            if itm not in cls.language:
                cls.language[itm] = cls.string_of_elements.count(itm)

    @classmethod
    def even_languages(cls):
        return ' '.join(key for key, value in cls.language.items() if value % 2 == 0)

    @classmethod
    def odd_languages(cls):
        return ' '.join(key for key, value in cls.language.items() if value % 2 != 0)


OddOccurrences.get_input()
print(OddOccurrences.odd_languages())
