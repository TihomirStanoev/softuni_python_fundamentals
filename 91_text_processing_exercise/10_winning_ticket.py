winning_symbols = {
    '@':[[],[]],
    '#':[[],[]],
    '$':[[],[]],
    '^':[[],[]]
}
def list_clear():
    global winning_symbols
    winning_symbols = {
        '@': [[], []],
        '#': [[], []],
        '$': [[], []],
        '^': [[], []]
    }


def is_valid(ticket_no):
    valid = False
    if len(ticket_no) == 20:
        valid = True
    return valid



def count_symbols(valid_ticket):

    half_of_ticket = [valid_ticket[:10], valid_ticket[10:]]

    for index, half in enumerate(half_of_ticket):
        last_symbol = ''
        for symbol in half:
            if symbol in winning_symbols.keys():
                if symbol == last_symbol:
                    winning_symbols[symbol][index][len(winning_symbols[symbol][index])-1] += 1
                else:
                    winning_symbols[symbol][index].append(1)
                    last_symbol = symbol
            else:
                last_symbol = symbol


def calculate_totals():


    for symbol, values in winning_symbols.items():
        if not winning_symbols[symbol][0]:
            winning_symbols[symbol][0] = 0
        else:
            winning_symbols[symbol][0] = max(values[0])

        if not winning_symbols[symbol][1]:
            winning_symbols[symbol][1] = 0
        else:
            winning_symbols[symbol][1] = max(values[1])



def check_symbol_points():
    winning_symbol = ''
    maximum_points = 0

    for symbol, points in winning_symbols.items():

        if points[0] < 6 or points[1] < 6:
            continue

        for point in points:
            if point >= maximum_points:
                maximum_points = point
                winning_symbol = symbol

    if maximum_points in range(6,10):
        return f'6{winning_symbol}'
    elif maximum_points == 10:
        return f'10{winning_symbol} Jackpot!'
    else:
        return 'no match'



tickets = input().split(', ')
tickets = list(map(lambda t: t.strip(), tickets))


for ticket in tickets:
    if not is_valid(ticket):
        print('invalid ticket')
        list_clear()
        continue

    else:
        count_symbols(ticket)
        print(f'ticket "{ticket}" - ', end='')

    calculate_totals()
    print(check_symbol_points())

    list_clear()
