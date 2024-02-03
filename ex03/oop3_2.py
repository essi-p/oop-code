class NumberStats:
    def __init__(self):
        self.total_numbers = 0
        self.sum_all = 0
        self.sum_even = 0
        self.sum_odd = 0

    def add_number(self, number: int):
        self.total_numbers += 1
        self.sum_all += number

        if number % 2 == 0:
            self.sum_even += number
        else:
            self.sum_odd += number

    def count_numbers(self):
        return self.total_numbers

    def get_sum(self):
        return self.sum_all

    def average(self):
        if self.total_numbers == 0:
            return 0
        return self.sum_all / self.total_numbers

if __name__ == "__main__":
    stats_all = NumberStats()
    stats_even = NumberStats()
    stats_odd = NumberStats()

    while True:
        user_input = int(input("Enter an integer (or -1 to stop): "))
        
        if user_input == -1:
            break

        stats_all.add_number(user_input)
        if user_input % 2 == 0:
            stats_even.add_number(user_input)
        else:
            stats_odd.add_number(user_input)

    print("All Numbers - Sum:", stats_all.get_sum())
    print("All Numbers - Mean:", stats_all.average())

    print("Even Numbers - Sum:", stats_even.get_sum())

    print("Odd Numbers - Sum:", stats_odd.get_sum())

