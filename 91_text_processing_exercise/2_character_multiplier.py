def calculate_sum(two_stings):
    first_string, second_string = two_stings

    first_ords = [ord(char) for char in first_string]
    second_ords = [ord(char) for char in second_string]

    total_sum = 0

    if len(first_ords) > len(second_ords):

        for _ in range(len(second_ords)):
            first_number = first_ords.pop(0)
            second_number = second_ords.pop(0)
            total_sum += first_number * second_number

        total_sum += sum(first_ords)

    elif len(first_ords) < len(second_ords):
        for _ in range(len(first_ords)):
            first_number = first_ords.pop(0)
            second_number = second_ords.pop(0)
            total_sum += first_number * second_number

        total_sum += sum(second_ords)
    else:
        for index in range(len(first_ords)):
            total_sum += first_ords[index] * second_ords[index]

    return total_sum



stings = input().split()
print(calculate_sum(stings))