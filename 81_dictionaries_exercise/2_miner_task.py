class MinerTask:

    def __init__(self):
        self.minerals = dict()

    def get_elements(self):

        while True:
            key = input()
            if key == 'stop':
                break
            value = int(input())

            if key not in self.minerals.keys():
                self.minerals[key] = value
            else:
                self.minerals[key] += value

    def __repr__(self):
        return '\n'.join(f'{key} -> {value}' for key, value in self.minerals.items())


mineral = MinerTask()
mineral.get_elements()
print(mineral)
