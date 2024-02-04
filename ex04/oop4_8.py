class Task:
    id_counter = 1

    def __init__(self, description, programmer, workload):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description, programmer, workload):
        self.tasks.append(Task(description, programmer, workload))
        print("added!")

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set(task.programmer for task in self.tasks))

    def mark_finished(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.finished = True
            print(f"marked as finished")
        else:
            raise ValueError("Task not found")

    def finished_orders(self):
        return [task for task in self.tasks if task.finished]

    def unfinished_orders(self):
        return [task for task in self.tasks if not task.finished]

    def status_of_programmer(self, programmer):
        tasks = [task for task in self.tasks if task.programmer == programmer]
        finished_tasks = [task for task in tasks if task.finished]
        unfinished_tasks = [task for task in tasks if not task.finished]
        finished_hours = sum(task.workload for task in finished_tasks)
        unfinished_hours = sum(task.workload for task in unfinished_tasks)
        return len(finished_tasks), len(unfinished_tasks), finished_hours, unfinished_hours


def main():
    orders = OrderBook()

    while True:
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

        command = input("command: ")

        if command == '0':
            break
        elif command == '1':
            try:
                description = input("description: ")
                programmer, workload = input("programmer and workload estimate: ").split()
                workload = int(workload)
                orders.add_order(description, programmer, workload)
            except (ValueError, TypeError):
                print("erroneous input")
        elif command == '2':
            finished_tasks = orders.finished_orders()
            for task in finished_tasks:
                print(task)
        elif command == '3':
            unfinished_tasks = orders.unfinished_orders()
            for task in unfinished_tasks:
                print(task)
        elif command == '4':
            try:
                task_id = int(input("id: "))
                orders.mark_finished(task_id)
            except ValueError:
                print("erroneous input")
        elif command == '5':
            programmers = orders.programmers()
            for programmer in programmers:
                print(programmer)
        elif command == '6':
            try:
                programmer = input("programmer: ")
                status = orders.status_of_programmer(programmer)
                print(status)
            except ValueError:
                print("erroneous input")


if __name__ == "__main__":
    main()
