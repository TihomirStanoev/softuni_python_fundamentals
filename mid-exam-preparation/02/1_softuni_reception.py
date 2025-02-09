employee_efficiency = [int(input()) for _ in range(3)]
total_students = int(input())


students_per_hour = sum(employee_efficiency)

hour = 0

while True:

    if total_students == 0:
        break

    hour += 1

    if hour % 4 == 0:
        continue


    if total_students <= students_per_hour:
        break

    total_students -= students_per_hour



print(f'Time needed: {hour:.0f}h.')