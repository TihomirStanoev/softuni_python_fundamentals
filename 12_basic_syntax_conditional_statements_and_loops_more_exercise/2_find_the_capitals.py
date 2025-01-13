word = input()

result = []
for ind, char in enumerate(word):
    if char.isupper():
        result.append(ind)

print(result)

