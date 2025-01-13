buget = int(input())
# command = input()
#
# while command != 'End':
#     price = int(command)
#     buget -= price
#     if buget < 0:
#         print('You went in overdraft!')
#         break
#     command = input()
# else:
#     print("You bought everything needed.")

command = input()
while True:
    price = int(command)
    buget -= price
    if buget < 0:
        print('You went in overdraft!')
        break
    command = input()
    if command == 'End':
        print("You bought everything needed.")
        break
