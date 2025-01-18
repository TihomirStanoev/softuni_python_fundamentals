key = int(input())
lines = int(input())


for _ in range(0,lines):
    letter = input() # P
    message_letter = ord(letter) + key
    print(chr(message_letter), end='')


