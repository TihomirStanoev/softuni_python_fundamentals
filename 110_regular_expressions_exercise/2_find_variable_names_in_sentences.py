import re

class VariableName:
    def __init__(self, sentanse):
        self.sentanse = sentanse

    def extract_variables(self):
        regex = r'\b_([A-Za-z]+)\b'
        variables = re.finditer(regex, self.sentanse)

        return ','.join(variable.group(1) for variable in variables)

my_string = input()

names = VariableName(my_string)

print(names.extract_variables())