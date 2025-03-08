class Contest:
    def __init__(self):
        self.passwords = {}

    def add_contest(self, contest, password):
        self.passwords[contest] = password

    def __str__(self):
        return '\n'.join(f'{contest} - {password}' for contest, password in self.passwords.items())


class Student:
    def __init__(self, username, contest, points):
        self.username = username
        self.contest = contest
        self.points = points


class Students:
    def __init__(self):
        self.results = {}

    def add_student(self, student, contest, points):
        points = int(points)
        if student in self.results.keys():
            if contest in self.results[student]:
                if points > self.results[student][contest]:
                    self.results[student][contest] = points
            else:
                self.results[student][contest] = points

        else:
            self.results[student] = {contest: points}

    def best_candidate(self):
        total_points = dict()

        for student, contests in self.results.items():
            total_points[student] = sum(contests.values())

        best_studnet = max(total_points, key=total_points.get)

        return f'Best candidate is {best_studnet} with total {total_points[best_studnet]} points.'

    def __str__(self):
        result = 'Ranking:\n'
        sorted_results = dict(sorted(self.results.items()))
        for student, contest in sorted_results.items():
            result += f'{student}\n'
            sorted_points = sorted(contest, key=contest.get, reverse=True)
            for cont in sorted_points:
                result += f'#  {cont} -> {contest[cont]}\n'
        return result


contests = Contest()
students = Students()

while True:
    command = input()
    if command == 'end of contests':
        break

    contest, passowrd = command.split(':')
    contests.add_contest(contest, passowrd)

while True:
    command = input()
    if command == 'end of submissions':
        break
    contest, password, name, points = command.split('=>')
    new_student = Student(name, contest, points)

    if contest not in contests.passwords.keys():
        continue

    if contests.passwords[contest] == password:
        students.add_student(new_student.username, new_student.contest, new_student.points)

print(students.best_candidate())
print(students)
