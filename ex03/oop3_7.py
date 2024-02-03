class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(person.height for person in self.persons)} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if not self.persons:
            return None
        return min(self.persons, key=lambda person: person.height)

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)
            return shortest_person
        else:
            return None

if __name__ == "__main__":
    # Testing the Room class
    room = Room()
    print("Is the room empty?", room.is_empty())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 175))

    print("Is the room empty?", room.is_empty())
    room.print_contents()

    print("Shortest:", room.shortest())

    removed = room.remove_shortest()
    if removed:
        print(f"Removed from room: {removed.name}")

    room.print_contents()
