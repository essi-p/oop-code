def smallest_average(person1: dict, person2: dict, person3: dict):
    def calculate_average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    averages = {
        "person1": calculate_average(person1),
        "person2": calculate_average(person2),
        "person3": calculate_average(person3)
    }

    min_person_key = min(averages, key=averages.get)
    return locals()[min_person_key]

person1 = {"name": "Alice", "result1": 8, "result2": 7, "result3": 9}
person2 = {"name": "Bob", "result1": 6, "result2": 8, "result3": 7}
person3 = {"name": "Charlie", "result1": 9, "result2": 5, "result3": 8}

winner = smallest_average(person1, person2, person3)
print(winner)
