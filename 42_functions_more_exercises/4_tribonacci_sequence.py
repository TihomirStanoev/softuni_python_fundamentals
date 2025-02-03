def tribonacci_sequence(number):
    numbers = [1]

    for _ in range(number - 1):

        if len(numbers) >= 3 + 1:
            b = sum(numbers[len(numbers) - 3:len(numbers)])
        else:
            b = sum(numbers)

        numbers.append(b)

    return numbers


number = int(input())

tribonacci_list = tribonacci_sequence(number)

print(' '.join(str(_) for _ in tribonacci_list))
