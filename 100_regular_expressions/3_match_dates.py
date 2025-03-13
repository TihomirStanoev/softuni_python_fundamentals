import re


dates = input()

regex = r'\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})\b'

re_dates = re.findall(regex, dates)


for date in re_dates:
    day, _, month, year = date
    print(f'Day: {day}, Month: {month}, Year: {year}')