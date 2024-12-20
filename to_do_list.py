class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = "Incomplete"
            print(f"Task '{task}' added to the to-do list.")
        else:
            print(f"Task '{task}' already exists in the to-do list.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = "Complete"
            print(f"Task '{task}' marked as complete.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def display_tasks(self):
        print("\nTo-Do List:")
        for task, status in self.tasks.items():
            print(f"{task}: {status}")
        print()


def main():
    to_do_list = ToDoList()

    while True:
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to mark as complete: ")
            to_do_list.complete_task(task)
        elif choice == "3":
            task = input("Enter the task to delete: ")
            to_do_list.delete_task(task)
        elif choice == "4":
            to_do_list.display_tasks()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
