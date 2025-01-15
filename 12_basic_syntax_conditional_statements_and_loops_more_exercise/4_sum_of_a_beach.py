given_string = input()

word = given_string.lower()

count = 0

for i, c in enumerate(word):
    #print(c)
    if c == 'w':
        if word[i:i+5] == 'water':
            count +=1
    if c == 's':
        if word[i:i+4] == 'sand':
            count +=1
        if word[i:i+3] == 'sun':
            count +=1
    if c == 'f':
        if word[i:i+4] == 'fish':
            count +=1


print(count)


