sequence = input().split()

sequence_integers = list(map(int,sequence))

even_number = lambda x: x % 2 == 0

even_list = list(filter(even_number, sequence_integers))

print(even_list)