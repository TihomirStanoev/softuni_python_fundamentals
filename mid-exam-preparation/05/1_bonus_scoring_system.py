from math import ceil

def higher_index(bonuses):
    max_value = max(bonuses)
    higher_index = bonuses.index(max_value)
    return higher_index, ceil(max_value)

def bonus_calculate(attendance, lectures, bonus):
    total_bonus = attendance / lectures * (5 + bonus)

    return total_bonus


def bonus_system(lectures, bonus, attendance_per_student):

    total_bonus_of_student = []
    for student in attendance_per_student:
        total_bonus_of_student.append(bonus_calculate(student,lectures,bonus))

    highest_bonus_index, highest_bonus = higher_index(total_bonus_of_student)
    highest_attendance = attendance_per_student[highest_bonus_index]

    return highest_bonus, highest_attendance


number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

attendance_of_each_student = [int(input()) for x in range(number_of_students)]


if number_of_students != 0:
    max_bonus, attended = bonus_system(number_of_lectures, additional_bonus, attendance_of_each_student)

else:
    max_bonus = 0
    attended = 0


print(f'Max Bonus: {max_bonus}.')
print(f'The student has attended {attended} lectures.')


