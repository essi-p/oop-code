import random

# Part 1: Simple dice
class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.current_side = 1

    def roll(self):
        self.current_side = random.randint(1, self.sides)

    def get_side(self):
        return self.current_side

def play_simple_dice_game(dices):
    results = [dice.get_side() for dice in dices]
    return sum(results), max(results)

# Part 2: Add dices
def create_dices(num_dices):
    return [Dice(6) for _ in range(num_dices)]

# Part 3: Add Players
class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice(6)

    def roll_dice(self):
        self.dice.roll()

    def __str__(self):
        return f"Player {self.player_id}: {self.name}, Dice Side: {self.dice.get_side()}"

def create_players(num_players):
    return [Player(f"Player {i}", i) for i in range(1, num_players + 1)]

# Part 4: Create a mammal object
class Mammal:
    def __init__(self, mammal_id, species, name, size, weight):
        self.mammal_id = mammal_id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

# Part 5: Add one data attribute to player
class PlayerWithPet(Player):
    def __init__(self, name, player_id):
        super().__init__(name, player_id)
        self.pet = None

    def assign_pet(self, mammal):
        self.pet = mammal

    def __str__(self):
        return f"Player {self.player_id}: {self.name}, Dice Side: {self.dice.get_side()}, Pet: {self.pet.name if self.pet else 'None'}"

# Part 6: Let the player select their pet mammal
def select_pet(player):
    dice1 = Dice(6)
    dice2 = Dice(6)
    dice1.roll()
    dice2.roll()
    sum_of_dices = dice1.get_side() + dice2.get_side()
    weight = random.uniform(1, sum_of_dices)
    mammal = Mammal
    player.assign_pet(mammal)

def main():
    num_dices = int(input("Enter the number of dices: "))
    dices = create_dices(num_dices)

    num_players = int(input("Enter the number of players: "))
    players = create_players(num_players)

    for player in players:
        player.roll_dice()
        print(player)

    for player in players:
        select_pet(player)
        print(player)

if __name__ == "__main__":
    main()
