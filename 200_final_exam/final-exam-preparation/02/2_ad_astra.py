import re


text_string = input()
daily_calories = 2000

pattern = r'([#\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

matches = re.findall(pattern, text_string)
total_cal = 0

foods = []

for match in matches:
    total_cal += int(match[3])
    foods.append([match[1],match[2],int(match[3])])

print(f'You have food to last you for: {total_cal//daily_calories} days!')
for food in foods:
    print(f'Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}')