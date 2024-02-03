class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95

    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount

if __name__ == "__main__":
    card = LunchCard(50)
    print(card)

    card.eat_ordinary()
    print(card)

    card.eat_luxury()
    card.eat_ordinary()
    print(card)

    try:
        card.deposit_money(-5)  # This should raise a ValueError
    except ValueError as e:
        print(e)

    card.deposit_money(15)
    print(card)

    card.deposit_money(10)
    print(card)

    card.deposit_money(200)
    print(card)
