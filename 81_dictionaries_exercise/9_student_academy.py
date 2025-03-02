from statistics import mean

higher_from = 4.50


def get_students(grades):
    students = dict()
    for _ in range(grades):
        student = input()
        grade = float(input())

        if student in students.keys():
            students[student].append(grade)
        else:
            students[student] = [grade]

    return students


def grade_filter(students_grade):
    for student, grades in students_grade.items():
        students_grade[student] = mean(grades)

    return '\n'.join(f'{st} -> {gr:.2f}' for st, gr in students_grade.items() if gr >= higher_from)


student_grade = int(input())

students_dict = get_students(student_grade)
print(grade_filter(students_dict))
