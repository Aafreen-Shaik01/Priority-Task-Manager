tasks = []

def add_task(name, priority):
    tasks.append({"name": name, "priority": priority})

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} (Priority: {task['priority']})")

def sort_tasks():
    tasks.sort(key=lambda x: x["priority"])

def search_task(name):
    for task in tasks:
        if task["name"].lower() == name.lower():
            return task
    return None

def delete_task(name):
    global tasks
    tasks = [t for t in tasks if t["name"].lower() != name.lower()]

def menu():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Sort Tasks\n4. Search Task\n5. Delete Task\n6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Task name: ")
            priority = int(input("Priority (lower = higher): "))
            add_task(name, priority)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            sort_tasks()
            print("Tasks sorted by priority.")

        elif choice == "4":
            name = input("Enter task name: ")
            result = search_task(name)
            print(result if result else "Task not found.")

        elif choice == "5":
            name = input("Enter task name to delete: ")
            delete_task(name)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")

menu()
