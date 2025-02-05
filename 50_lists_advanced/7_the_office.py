from statistics import mean

employees = list(map(int,input().split()))


factor = int(input())

more_happy = [employee * factor for employee in employees]
most_happy = list(filter(lambda e: e > mean(more_happy), more_happy))



total_employees = len(more_happy)
total_happy = len(most_happy)

if total_happy < total_employees / 2:
    print(f'Score: {total_happy}/{total_employees}. Employees are not happy!')
else:
    print(f'Score: {total_happy}/{total_employees}. Employees are happy!')
