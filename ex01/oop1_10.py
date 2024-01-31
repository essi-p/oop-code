class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print("Ok!")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}{self.contacts[name]}")
        else:
            print(f"{name}no number")

def phone_book_app():
    phone_book = PhoneBook()

    while True:
        print("command (1 search, 2 add, 3 quit):")
        command = int(input())

        if command == 1:
            name = input("name: ")
            phone_book.search_contact(name)
        elif command == 2:
            name = input("name: ")
            number = input("number: ")
            phone_book.add_contact(name, number)
        elif command == 3:
            print("quitting...")
            break
        else:
            print("Invalid command. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    phone_book_app()
