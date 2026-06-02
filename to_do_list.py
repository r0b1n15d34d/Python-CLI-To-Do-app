print("Hello, welcome to the To-Do list app!")

tasks = []

def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")

try:
    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = [task.strip() for task in file.readlines()]

except FileNotFoundError:
    tasks = []
    save_tasks()


def add_task():
    while True:
        user_input = input("Please enter a task: ")
        tasks.append(user_input)
        save_tasks()
        print(f"'{user_input}' is added to the list")
        another = input("Would you like to add another task? y/n")
        if another == "n":
            break

def view_tasks(pause=True):
    print("To-Do list: ")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    if pause:
       input("\nPress enter to continue...")    


def mark_tasks():
    if not tasks:
        print("No tasks to mark!")
        input("\nPress enter to continue...")
        return
    view_tasks(pause=False)
    mark_task = int(input("Which task number would you like to mark as done? "))
    if tasks[mark_task - 1].startswith("✅"):
        print("That task is already marked!")
        input("\nPress enter to continue...")
        return
    tasks[mark_task - 1] = f"✅ {tasks[mark_task - 1]}"
    marked = tasks[mark_task - 1]
    save_tasks()
    print(f"{marked} is checked")
    input("\nPress enter to continue...")




def delete_task():
    if not tasks:
        print("No tasks to delete!")
        input("\nPress enter to continue...")
        return
    view_tasks(pause=False)
    task_del = int(input("Which task number would you like to delete?"))
    deleted = tasks.pop(task_del - 1)
    save_tasks()
    print(f"{deleted} is deleted from the list")
    input("\nPress enter to continue...")

while True:
    print("1. add task")
    print("2. view tasks")
    print("3. mark a task")
    print("4. delete task")
    print("5. quit")
    user_choice = input("Choose one of the following: ")
    if user_choice == "1":
        add_task()
    elif user_choice == "2":
        view_tasks()
    elif user_choice == "3":
        mark_tasks()    
    elif user_choice == "4":
        delete_task()
    elif user_choice == "5":
        print("Have a nice day!")
        break    
    else:
        print("invaild choice, please try again!")





    
        
