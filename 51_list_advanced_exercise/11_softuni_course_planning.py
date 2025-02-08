# 88 / 100

def not_exist(given_lessons, lesson):
    if lesson not in given_lessons:
        return True
    return False

def sort_exercise(list_for_sort):
    for lesson_index,lesson in enumerate(list_for_sort):
        for exercise_index, exercise in enumerate(list_for_sort):
            if exercise == f'{lesson}-Exercise':
                list_for_sort.pop(exercise_index)
                list_for_sort.insert(lesson_index+1,exercise)

    return list_for_sort


lessons_list = input().split(', ')


while True:
    command = input().split(':')
    if command[0] == 'course start':
        break

    action = command[0]
    lesson_title = command[1]

    if action == 'Add':
        if not_exist(lessons_list, lesson_title):
            lessons_list.append(lesson_title)

    elif action == 'Insert':
        if not_exist(lessons_list, lesson_title):
            given_index = int(command[2])
            lessons_list.insert(given_index, lesson_title)

    elif action == 'Remove':
        if not not_exist(lessons_list, lesson_title):
            lessons_list.remove(lesson_title)

    elif action == 'Swap':
        second_lesson_title = command[2]
        if not not_exist(lessons_list, lesson_title) and not not_exist(lessons_list, second_lesson_title):
            first_lesson_index = lessons_list.index(lesson_title)
            second_lesson_index = lessons_list.index(second_lesson_title)
            lessons_list[first_lesson_index], lessons_list[second_lesson_index] = lessons_list[second_lesson_index], lessons_list[first_lesson_index]
            lessons_list = sort_exercise(lessons_list)

    elif action == 'Exercise':
        exercise = f'{lesson_title}-Exercise'
        if not not_exist(lessons_list, lesson_title):
            lesson_index = lessons_list.index(lesson_title)
            lessons_list.insert(lesson_index+1, exercise)
        else:
            lessons_list.append(lesson_title)
            lessons_list.append(exercise)


[print(f'{position+1}.{lesson}') for position, lesson in enumerate(lessons_list)]