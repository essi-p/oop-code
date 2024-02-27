class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"card balance is {self.balance:.1f} euros")
            return True
        else:
            print("payment successful: false")
            return False

    def deposit_money(self, amount: float):
        self.balance += amount


class PaymentTerminal:
    def __init__(self):
        self.cash_balance = 1000  
        self.regular_lunches_sold = 0
        self.special_lunches_sold = 0

    def pay_cash(self, amount: float):
        if self.cash_balance >= amount:
            self.cash_balance -= amount
            print("payment successful: true")
            return True
        else:
            print("payment successful: false")
            return False

    def eat_lunch_with_card(self, card: LunchCard, price: float):
        if card.subtract_from_balance(price):
            if price == 5.0:  
                self.special_lunches_sold += 1
            else:
                self.regular_lunches_sold += 1
            print("payment successful: true")
        else:
            print("payment successful: false")

    def deposit_money_to_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.cash_balance += amount
        print(f"Deposited {amount:.1f} euros to the card. New card balance: {card.balance:.1f} euros")

if __name__ == "__main__":
    # Part 4: Depositing money on the card
    terminal = PaymentTerminal()
    card = LunchCard(5)

    card.subtract_from_balance(5.0)
    terminal.eat_lunch_with_card(card, 4.5)

    card.deposit_money(100)
    terminal.eat_lunch_with_card(card, 5.3)

    print(f"Funds available in the terminal: {terminal.cash_balance}")
    print(f"Regular lunches sold: {terminal.regular_lunches_sold}")
    print(f"Special lunches sold: {terminal.special_lunches_sold}")
