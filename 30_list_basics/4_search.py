number = int(input())
word = input()

list_with_words = [input() for words in range(number)]

filtered_list = []
for paragraph in list_with_words:
    if word in paragraph:
        filtered_list.append(paragraph)

print(list_with_words)
print(filtered_list)