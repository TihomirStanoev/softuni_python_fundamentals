# car_dict = {'car_name': {'mileage': 0, 'fuel': 0}}
max_tank_capacity = 75
car_dict = dict()


def drive(the_car, drive_distance, need_fuel):
    global car_dict
    current_fuel = car_dict[the_car]['fuel']
    message = ''

    if current_fuel >= need_fuel:
        car_dict[the_car]['fuel'] -= need_fuel
        car_dict[the_car]['mileage'] += drive_distance
        message += f'{the_car} driven for {drive_distance} kilometers. {need_fuel} liters of fuel consumed.\n'

        if car_dict[the_car]['mileage'] >= 100_000:
            del car_dict[the_car]
            message += f'Time to sell the {the_car}!'

    else:
        message += "Not enough fuel to make that ride"

    return message.strip()


def refuel(the_car, ref_fuel):
    global car_dict
    tank_fuel = car_dict[the_car]['fuel']
    refueled_fuel = 0

    if tank_fuel + ref_fuel <= max_tank_capacity:
        car_dict[the_car]['fuel'] += ref_fuel
        refueled_fuel = ref_fuel
    else:
        car_dict[the_car]['fuel'] = max_tank_capacity
        refueled_fuel = max_tank_capacity - tank_fuel

    return f'{the_car} refueled with {refueled_fuel} liters'


def revert(the_car, kilometers):
    global car_dict
    car_mileage = car_dict[the_car]['mileage']
    message = ''

    if car_mileage - kilometers <= 10_000:
        car_dict[the_car]['mileage'] = 10_000
    else:
        car_dict[the_car]['mileage'] -= kilometers
        message = f"{the_car} mileage decreased by {kilometers} kilometers"

    return message


total_cars = int(input())

for _ in range(total_cars):
    car = input().split('|')
    name = car[0]
    mileage = int(car[1])
    fuel = int(car[2])
    car_dict[name] = {'mileage': mileage, 'fuel': fuel}

while True:
    commands = input()
    if commands == 'Stop':
        break
    split_command = commands.split(' : ')

    command = split_command[0]
    car = split_command[1]

    if command == 'Drive':
        distance = int(split_command[2])
        fuel = int(split_command[3])
        print(drive(car, distance, fuel))


    elif command == 'Refuel':
        fuel = int(split_command[2])
        print(refuel(car, fuel))

    elif command == 'Revert':
        distance = int(split_command[2])
        result = revert(car, distance)
        if result:
            print(result)

for car_key in car_dict.keys():
    car = car_key
    mileage = car_dict[car]['mileage']
    total_fuel = car_dict[car]['fuel']

    print(f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {total_fuel} lt.')

