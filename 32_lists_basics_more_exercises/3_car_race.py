def time_cal(car_times):
    total_time = 0
    for sec in car_times:
        if sec != 0:
            total_time += sec
        else:
            total_time *= 0.8

    return total_time


time_str = input().split()

time_list = [int(sec) for sec in time_str]

middle = len(time_list)//2


left_car_times = []

for index in range(middle):
    left_car_times.append(time_list[index])

right_car_times = []
for index in range(len(time_list)-1, middle, -1):
    right_car_times.append(time_list[index])


left_car_time = time_cal(left_car_times)
right_car_time = time_cal(right_car_times)

if left_car_time < right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
else:
    print(f'The winner is right with total time: {right_car_time:.1f}')