def statistic_dict():
    statistic = {}

    while True:
        command = input().split(": ")
        key = command[0]

        if key == 'statistics':
            break
        value = int(command[1])

        if key in statistic.keys():
            statistic[key] += value

        else:
            statistic[key] = int(value)

    return statistic


def dict_items(stat_dict):
    return '\n'.join(f'- {key}: {value}' for key, value in stat_dict.items())


def totals(stat_dict):
    return f'Total Products: {len(stat_dict)}\nTotal Quantity: {sum(stat_dict.values())}'


dict_statistics = statistic_dict()

print('Products in stock:')
print(dict_items(dict_statistics))
print(totals(dict_statistics))
