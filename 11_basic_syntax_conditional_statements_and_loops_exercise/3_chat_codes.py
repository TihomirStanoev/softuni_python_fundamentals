number_of_messages = int(input())

# •	If the number is 88 - "Hello"
# •	If the number is 86 - "How are you?"
# •	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
# •	If the number is over 88 - "Bye."

for _ in range(number_of_messages):
    number = int(input())

    if number == 86:
        print("How are you?")
    elif number == 88:
        print("Hello")
    elif number < 88:
        print("GREAT!")
    else:
        print("Bye.")