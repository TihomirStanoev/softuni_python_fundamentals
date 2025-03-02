class Parking:
    def __init__(self, name, commands):
        self.name = name
        self.commands = commands
        self.database = dict()

    def register(self, username, plate):

        if username in self.database.keys():
            return f'ERROR: already registered with plate number {plate}'
        else:
            self.database[username] = plate
        return f'{username} registered {plate} successfully'

    def unregister(self, username):

        if username not in self.database.keys():
            return f'ERROR: user {username} not found'
        else:
            del self.database[username]
            return f"{username} unregistered successfully"

    def __str__(self):
        return '\n'.join(f'{user} => {plate}' for user,plate in self.database.items())



total_commands = int(input())
softuni = Parking('SoftUni', total_commands)

for _ in range(softuni.commands):
    comd = input().split()

    command = comd[0]
    name = comd[1]

    if command == 'register':
        license_plate = comd[2]
        print(softuni.register(name, license_plate))

    elif command == 'unregister':
        print(softuni.unregister(name))

print(softuni)
