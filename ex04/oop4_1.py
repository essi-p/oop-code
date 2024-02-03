class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None

        frequency_dict = {}
        for item in my_list:
            frequency_dict[item] = frequency_dict.get(item, 0) + 1

        max_frequency_item = max(frequency_dict, key=frequency_dict.get)
        return max_frequency_item

    @classmethod
    def doubles(cls, my_list: list):
        if not my_list:
            return 0

        unique_items = set(my_list)
        count = 0
        for item in unique_items:
            if my_list.count(item) >= 2:
                count += 1

        return count

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
