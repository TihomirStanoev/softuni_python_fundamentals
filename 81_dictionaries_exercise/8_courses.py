def register_students():
    courses = dict()
    while True:
        command = input().split(' : ')
        if 'end' in command:
            break
        course, student = command

        if course not in courses.keys():
            courses[course] = [student]
        else:
            courses[course].append(student)

    return courses


students = register_students()

for course, all_students in students.items():
    print(f'{course}: {len(students[course])}')
    for student in students[course]:
        print(f'-- {student}')
