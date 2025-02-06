containing_strings = input().split(', ')
second_input_line = input().split(', ')

final_list = []
contained_strings = [final_list.append(string) for string in containing_strings for words in second_input_line if string in words if string not in final_list]


print(final_list)