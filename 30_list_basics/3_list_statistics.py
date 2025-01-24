numbers = int(input())


positives_list = []
negatives_list = []

for number in range(numbers):
    x = int(input())
    if x < 0:
        negatives_list.append(x)
    else:
        positives_list.append(x)

print(positives_list)
print(negatives_list)
print(f'Count of positives: {len(positives_list)}')
print(f'Sum of negatives: {sum(negatives_list)}')