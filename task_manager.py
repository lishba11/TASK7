from file_handler import read_tasks, write_tasks
from task_operations import add_task, remove_task, update_task, view_tasks

def main():
    file_path = "tasks.txt"
    tasks = read_tasks(file_path)

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks = add_task(tasks, task)
            write_tasks(file_path, tasks)
        elif choice == "2":
            view_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to remove: "))
                tasks = remove_task(tasks, task_number)
                write_tasks(file_path, tasks)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                tasks = update_task(tasks, task_number, new_task)
                write_tasks(file_path, tasks)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
