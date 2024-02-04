class Computer:
    def __init__(self, model: str, speed: int):
        self.model = model
        self.speed = speed

    def __str__(self):
        return f"{self.model}, {self.speed} MHz"


class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self.weight = weight

    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"


if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)
