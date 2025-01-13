command = input()


while command != "End":

    string = ""
    if command == "SoftUni":
        command = input()
        continue

    for char in command:
        string += char*2

    print(string)

    command = input()



