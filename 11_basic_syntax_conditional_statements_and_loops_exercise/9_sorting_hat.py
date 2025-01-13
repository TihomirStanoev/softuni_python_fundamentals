command = input()


while command != "Welcome!":

    if command == "Voldemort":
        break

    name_length = len(command)
    school = ''

    if name_length == 5:
        school = command + " goes to Slytherin."
    elif name_length == 6:
        school = command + " goes to Ravenclaw."
    elif name_length > 6:
        school = command + " goes to Hufflepuff."
    else:
        school = command + " goes to Gryffindor."

    print(school)
    command = input()

if command == "Voldemort":
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
