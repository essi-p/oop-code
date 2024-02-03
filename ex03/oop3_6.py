# Part 1: The Present class
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} g)"


# Part 2: The Box class
class Box:
    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        return sum(present.weight for present in self.presents)


if __name__ == "__main__":
    book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:", book)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 50)
    box.add_present(cd)
    print(box.total_weight())
