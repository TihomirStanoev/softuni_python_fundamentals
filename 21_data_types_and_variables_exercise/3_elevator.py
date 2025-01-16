from math import ceil

capacity = int(input())
persons = int(input())

courses = ceil(capacity / persons)

print(courses)