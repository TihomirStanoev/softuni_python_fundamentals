number_of_electrons = int(input())



shells = []
position_of_shell = 1

while number_of_electrons > 0:
    electrons = 2 * position_of_shell ** 2
    position_of_shell += 1

    shells.append(number_of_electrons) if electrons >= number_of_electrons else shells.append(electrons)

    number_of_electrons -= electrons


print(shells)