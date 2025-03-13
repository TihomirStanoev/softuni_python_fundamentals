import re


numbers = input()

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?(\.\d+)?($|(?=\s))"

matches = re.finditer(regex, numbers)

print(' '.join(match.group() for match in matches))