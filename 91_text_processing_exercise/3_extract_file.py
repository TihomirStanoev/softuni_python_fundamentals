class NameExtractor:
    def __init__(self, file_path):
        self.file_path = file_path.split('\\')[-1]

    def file_name(self):
        name = self.file_path.split('.')
        return name[-2]

    def extension(self):
        name = self.file_path.split('.')
        return name[-1]



path_of_file = input()
file = NameExtractor(path_of_file)

print(f'File name: {file.file_name()}')
print(f'File extension: {file.extension()}')