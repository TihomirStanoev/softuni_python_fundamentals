def corresponding_words(grande_number):
    word = ''

    if 2.00 <= grande_number <= 2.99:
        word = "Fail"
    elif 3.00 <= grande_number <= 3.49:
        word = "Poor"
    elif 3.50 <= grande_number <= 4.49:
        word = "Good"
    elif 4.50 <= grande_number <= 5.49:
        word = "Very Good"
    elif 5.50 <= grande_number <= 6.00:
        word = "Excellent"

    return word



grade = float(input())

grade_words = corresponding_words(grade)

print(grade_words)