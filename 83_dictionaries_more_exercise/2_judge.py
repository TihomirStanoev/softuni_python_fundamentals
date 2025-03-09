class Judge:
    def __init__(self):
        self.result = dict()
        self.individual_results = dict()

    def add_student(self, name, contest, points):
        points = int(points)

        if contest not in self.result:
            self.result[contest] = {}

        if name not in self.result[contest]:
            self.result[contest][name] = points
        else:
            if self.result[contest][name] < points:
                self.result[contest][name] = points

    def contest_results(self):
        result = ''
        for contest, students in self.result.items():
            sorted_students = sorted(students.items(), key=lambda x: (-x[1], x[0]))
            result += f'{contest}: {len(sorted_students)} participants\n'
            for i, (student, points) in enumerate(sorted_students, start=1):
                result += f'{i}. {student} <::> {points}\n'

        return result.strip()

    def individual_statistics(self):
        result = 'Individual standings:\n'
        for students in self.result.values():
            for student, points in students.items():
                if student not in self.individual_results:
                    self.individual_results[student] = points
                else:
                    self.individual_results[student] += points

        sorted_individuals = sorted(self.individual_results.items(), key=lambda x: (-x[1], x[0]))

        for i, (student, total_points) in enumerate(sorted_individuals, start=1):
            result += f'{i}. {student} -> {total_points}\n'

        return result.strip()


judge = Judge()

while True:
    command = input()
    if command == 'no more time':
        break

    username, contest, points = command.split(' -> ')
    judge.add_student(username, contest, points)

print(judge.contest_results())
print(judge.individual_statistics())