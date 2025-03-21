students_results = dict()
students_ban = []


def register_result(username, technology, grade):
    if username not in students_results.keys():
        students_results[username] = {technology: [grade]}
    elif username in students_results.keys():
        if technology in students_results[username].keys():
            students_results[username][technology].append(grade)
        elif technology not in students_results[username].keys():
            students_results[username][technology]= [grade]


def banned_students(name):
    students_ban.append(name)


def higher_scores():
    result = 'Results:\n'
    best_result = dict()
    for student, tech in students_results.items():
        best_result[student] = dict()
        for technology, grade in tech.items():
            best_result[student][technology] = max(grade)

    higher_grade_per_lang = dict()
    for student, technology in best_result.items():
        if student in students_ban:
            continue
        max_scores = 0
        for tech, score in technology.items():
            if score >= max_scores:
                max_scores = score
        higher_grade_per_lang[student] = max_scores
    result += ('\n').join(f'{name} | {max_grade}' for name, max_grade in higher_grade_per_lang.items())

    return result

def submissions():
    result = 'Submissions:\n'
    languages = dict()
    for student, tech in students_results.items():
        for technology, grades in tech.items():
            if technology not in languages.keys():
                languages[technology] = len(grades)
            else:
                languages[technology] += len(grades)

    result += ('\n').join(f'{tec} - {cont}' for tec, cont in languages.items())

    return result

def main():
    while True:
        commnad = input().split('-')
        if 'exam finished' in commnad:
            break

        if commnad[1] == 'banned':
            user = commnad[0]
            banned_students(user)

        else:
            user, technology, points = commnad
            points = int(points)
            register_result(user, technology, points)

    print(higher_scores())
    print(submissions())

if __name__ == "__main__":
    main()
