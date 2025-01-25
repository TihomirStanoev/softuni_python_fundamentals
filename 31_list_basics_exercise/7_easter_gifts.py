gifts = input().split()



command = input()

while command != 'No Money':
    commands_list = command.split()

    command = commands_list[0]
    given_gift = commands_list[1]

    if command == 'OutOfStock':
        for gift in range(gifts.count(given_gift)):
            index = gifts.index(given_gift)
            gifts[index] = "None"


    elif command == 'Required':
        index = int(commands_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = given_gift


    elif command == 'JustInCase':
        gifts[-1] = given_gift


    command = input()

final_list = [gift for gift in gifts if gift != "None"]


print(" ".join(gift for gift in final_list))
