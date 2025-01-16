starting_char = int(input())
ending_char = int(input())


char_range = (ending_char - starting_char)+1

for char in range(char_range):
    print(chr(starting_char), end=" ")
    starting_char += 1