class Car:
    max_fuel_capacity = 75

    def __init__(self, brand: str, mileage: int, fuel: int):
        self.brand = brand
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, km: int, needed_fuel: int) -> str:
        message = ''
        if self.fuel >= needed_fuel:
            self.mileage += km
            self.fuel -= needed_fuel
            message = f'{self.brand} driven for {km} kilometers. {needed_fuel} liters of fuel consumed.'

        else:
            message = "Not enough fuel to make that ride"

        return message

    def refuel(self, ref_fuel: int) -> str:
        refueled_fuel = 0

        if self.fuel + ref_fuel <= Car.max_fuel_capacity:
            self.fuel += ref_fuel
            refueled_fuel = ref_fuel

        else:
            refueled_fuel = Car.max_fuel_capacity - self.fuel
            self.fuel = Car.max_fuel_capacity

        return f'{self.brand} refueled with {refueled_fuel} liters'

    def revert(self, kilometers: int) -> str:
        result = ''
        if self.mileage - kilometers <= 10_000:
            self.mileage = 10_000
        else:
            self.mileage -= kilometers
            result = f"{self.brand} mileage decreased by {kilometers} kilometers"

        return result


class Garage:
    car_id = 0

    def __init__(self):
        self.cars = dict()

    def add_car(self, new_car):
        if new_car.fuel < Car.max_fuel_capacity:
            self.cars[new_car.brand] = new_car

    def getting_car(self, name: str):

        taken_car = self.cars[name]
        self.cars[name] = None

        return taken_car

    def return_car(self, car):
        message = ''

        if car.mileage >= 100_000:
            print(f'Time to sell the {car.brand}!')
        else:
            self.cars[car.brand] = car

    def print_cars(self):
        result = ''

        for name, car in self.cars.items():
            if car is not None:
                result += f'{car.brand} -> Mileage: {car.mileage} kms, Fuel in the tank: {car.fuel} lt.\n'

        return result.strip()


garage = Garage()

added_car = int(input())

for _ in range(added_car):
    car_line = input().split('|')
    new_name = car_line[0]
    new_mileage = int(car_line[1])
    new_fuel = int(car_line[2])

    car_new = Car(new_name, new_mileage, new_fuel)
    garage.add_car(car_new)

while True:
    commands = input()
    if commands == 'Stop':
        break
    split_command = commands.split(' : ')

    command = split_command[0]
    get_car = split_command[1]
    current_car = garage.getting_car(get_car)

    if command == 'Drive':
        distance = int(split_command[2])
        tank = int(split_command[3])
        print(current_car.drive(distance, tank))

    elif command == 'Refuel':
        tank = int(split_command[2])
        print(current_car.refuel(tank))

    elif command == 'Revert':
        distance = int(split_command[2])
        revert = current_car.revert(distance)
        if revert:
            print(revert)

    garage.return_car(current_car)

print(garage.print_cars())
