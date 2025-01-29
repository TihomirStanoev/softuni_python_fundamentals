def loading_bar(progress):
    bar, status = '', ''

    dots = progress // 10

    for fill in range(1,11):
        if fill <= dots:
            bar += '%'
        else:
            bar += '.'

    if progress == 100:
        bar = '100% Complete!'
        status = '[%%%%%%%%%%]'
    else:
        bar = f'{progress}% [{bar}]'
        status = 'Still loading...'

    return bar, status



number = int(input())

bar_progress, status_time = loading_bar(number)

print(bar_progress)
print(status_time)