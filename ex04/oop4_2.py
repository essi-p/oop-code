class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} g)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def __str__(self):
        item_count = len(self.__items)
        combined_weight = self.weight()
        return f"{item_count} {'item' if item_count == 1 else 'items'} ({combined_weight} g)"

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        return max(self.__items, key=lambda item: item.weight())


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def __str__(self):
        suitcase_count = len(self.__suitcases)
        available_space = self.__max_weight - self.weight()
        return f"{suitcase_count} {'suitcase' if suitcase_count == 1 else 'suitcases'}, space for {available_space:.1f} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.__suitcases)

    def heaviest_item(self):
        heaviest_items = [suitcase.heaviest_item() for suitcase in self.__suitcases if suitcase.heaviest_item()]
        if not heaviest_items:
            return None
        return max(heaviest_items, key=lambda item: item.weight())


if __name__ == "__main__":
    # Testing the classes
    book = Item("ABC Book", 200)
    phone = Item("Nokia 3210", 100)
    brick = Item("Brick", 400)

    adas_suitcase = Suitcase(1000)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(1000)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(100)
    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
