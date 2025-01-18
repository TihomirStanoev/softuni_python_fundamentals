lines = int(input())

brakets = ''

for char in range(lines):
    command = input()
    if command == "(" or command == ")":
        brakets += command

list_braket = []
for i in range(0, len(brakets), 2):
    list_braket.append(brakets[i:i + 2])

is_balanced = True

for brk in list_braket:
    if brk != "()":
        is_balanced = False
        break

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')




