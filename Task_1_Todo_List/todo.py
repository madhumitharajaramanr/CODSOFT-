tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added ✅")

    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            for i, t in enumerate(tasks, start=1):
                print(i, t)

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted ✅")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
