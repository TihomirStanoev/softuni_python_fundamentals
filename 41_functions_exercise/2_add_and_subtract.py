def add_and_subtract(first, second, third):
    def sum_numbers(f, s):
        return f+s

    def subtract(result, t):
        return result - t

    sums = sum_numbers(first,second)
    end_result = subtract(sums, third)

    return end_result





a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a,b,c))