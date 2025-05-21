import json
FILENAME = "tasks.json"
def load_tasks():
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)
def To_Do_List():
    tasks = load_tasks()
    print("\n___TO-DO-LIST MENU___")
    print("choices:")
    print("1. Add new task")
    print("2. View all task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
    while True:
        choice = input("Enter your choice to do(1-5): ")
        print("")
        if choice == "1":
            task = input("Enter task: ").lower()
            time = input("Set time: ").lower()
            tasks.append({'Task': task, 'Time': time, 'Due': 'Due!'})
            print("Task added sucessfully!")
            print("-"*40)
            save_tasks(tasks)
        elif choice == "2":
            if not tasks:
                print("No task present")
                print("-"*40)
            else:
                for i, t in enumerate(tasks, start = 1):
                    print(f"{i}. Task: {t['Task']},  Time: {t['Time']}, Status: {t['Due']}")
                print("-"*40)
        elif choice == "3":
            done = input("Enter a task to mark it as complete: ").lower()
            found = False
            for i in tasks:
                if i['Task'] == done:
                    i['Due'] = 'Completed!'
                    print("Congratulation! task completed successfully")
                    print("-"*40)
                    found = True
                    break
            save_tasks(tasks)
            if not found:
                print("Task not found!")
                print("-"*40)
        elif choice == "4":
            delete = input("Enter a task to delete it: ").lower()
            found = False
            for i in tasks:
                if i['Task'] == delete:
                    tasks.remove(i)
                    print("Task deleted succesfully!")
                    print("-"*40)
                    found = True
                    break
            save_tasks(tasks)
            if not found:
                print("Task not found!")
                print("-"*40)
        elif choice == "5":
            print("Thank You for using To_Do_List!")
            print("-"*40)
            break
        else:
            print("Invalid choice\nPlease enter a valid choice(1-5)")
            print("-"*40)
                    
To_Do_List()