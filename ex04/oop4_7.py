class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None

    def name(self):
        return self._name

    def numbers(self):
        return self._numbers

    def address(self):
        return self._address

    def add_number(self, number):
        self._numbers.append(number)

    def add_address(self, address):
        self._address = address


class PhoneBook:
    def __init__(self):
        self._persons = {}

    def add_number(self, name, number):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_number(number)

    def add_address(self, name, address):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_address(address)

    def get_entry(self, name):
        if name in self._persons:
            person = self._persons[name]
            return person.name(), person.numbers(), person.address()
        return None, "number unknown", "address unknown"


def main():
    phonebook = PhoneBook()

    while True:
        print("commands:")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

        command = input("command: ")

        if command == '0':
            break
        elif command == '1':
            name = input("name: ")
            number = input("number: ")
            phonebook.add_number(name, number)
        elif command == '2':
            name = input("name: ")
            name, number, address = phonebook.get_entry(name)
            print(name)
            print(number)
            print(address)
        elif command == '3':
            name = input("name: ")
            address = input("address: ")
            phonebook.add_address(name, address)


if __name__ == "__main__":
    main()
