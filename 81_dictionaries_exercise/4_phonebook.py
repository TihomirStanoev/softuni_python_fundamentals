class Phonebook:
    def __init__(self):
        self.phonebook = dict()
        self.contacts = []
        self.number_of_contacts = 0

    def rec_numbers(self):
        while True:
            command = input()
            if '-' not in command:
                self.number_of_contacts = int(command)
                break
            contact, phone = command.split('-')
            self.phonebook[contact] = phone

    def contacts_for_search(self):
        for _ in range(self.number_of_contacts):
            contact = input()
            self.contacts.append(contact)

    def __str__(self):
        phones = ''
        for contact in self.contacts:
            if contact in self.phonebook.keys():
                phones += f'{contact} -> {self.phonebook[contact]}\n'
            else:
                phones += f'Contact {contact} does not exist.\n'

        return phones


my_phonebook = Phonebook()
my_phonebook.rec_numbers()
my_phonebook.contacts_for_search()
print(my_phonebook)