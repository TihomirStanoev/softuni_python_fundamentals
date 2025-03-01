class Capitals:
    def __init__(self):
        self.countries = []
        self.capitals = []
        self.capitals_dict = dict()

    def get_countries(self, countries_str):
        self.countries = countries_str.split(', ')

    def get_capitals(self, capital_str):
        self.capitals = capital_str.split(', ')

    def __repr__(self):
        self.capitals_dict = dict(zip(self.countries, self.capitals))
        return '\n'.join(f'{country} -> {capital}' for country, capital in self.capitals_dict.items())


countries_format = Capitals()
countries_string = input()
countries_format.get_countries(countries_string)
capitals_string = input()
countries_format.get_capitals(capitals_string)

print(countries_format)
