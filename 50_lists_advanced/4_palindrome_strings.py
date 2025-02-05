words_list = list(input().split())
palindrome = input()


palindromes = [word for word in words_list if word[::-1] == word]

occurrences = palindromes.count(palindrome)

print(palindromes)
print(f'Found palindrome {occurrences} times')