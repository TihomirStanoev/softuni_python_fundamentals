class Students:
    def __init__(self):
        self.dict_students = {}
        self.course = ''


    def get_input(self):
        while True:
            command = input().split(':')

            if len(command) == 1:
                self.course = command[0]
                break

            student_name, student_id, new_course = command
            new_course = new_course.replace(' ', '_')
            student_id = int(student_id)

            if new_course in self.dict_students:
                self.dict_students[new_course].extend([student_name, student_id])
            else:
                self.dict_students[new_course] = [student_name, student_id]


    def course(self):
        return self.course

    def result(self, target_course):
        result = ''

        for i in range(0, len(self.dict_students[target_course]),2):
            result += f'{self.dict_students[target_course][i]} - {self.dict_students[target_course][i+1]}\n'

        return result




first_try = Students()
first_try.get_input()
course = first_try.course
print(first_try.result(course))
