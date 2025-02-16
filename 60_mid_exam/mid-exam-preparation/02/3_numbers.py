from statistics import mean

numbers = list(map(int,input().split()))

average_value = round(mean(numbers),2)
numbers.sort(reverse=True)

top_counter = 5
top_values = []
lower_that_5 = False
for number in numbers:
    if number > average_value:
        top_values.append(number)
        top_counter -= 1
        if top_counter == 0:
            break
    else:
        lower_that_5 = True

if not top_values and lower_that_5:
    print('No')
else:
    print(' '.join(str(x) for x in top_values))