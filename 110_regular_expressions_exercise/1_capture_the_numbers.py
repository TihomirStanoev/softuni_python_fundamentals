import re

class Numbers:
    def __init__(self, text):
        self.text = text

    def extract_numbers(self):
        regex = r'\d+'
        nums = re.findall(regex, self.text)
        return ' '.join(nums)


my_string = ''
while True:
    user_input = input()
    if not user_input:
        break
    my_string += user_input

numbers = Numbers(my_string)

print(numbers.extract_numbers())