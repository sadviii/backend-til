"""Build a small Task Manager console application.

Your application should be able to:
Add a task
View all tasks
Mark a task as completed
Exit

Your program should have a menu like:

===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Exit

Enter your choice:
Example interaction
Enter your choice: 1
Enter task: Learn Python
Task added!

Enter your choice: 2

1. [ ] Learn Python

Enter your choice: 3
Enter task number: 1
Task completed!

Enter your choice: 2

1. [✓] Learn Python
🚨 But here's the important part

I am NOT going to give you the code.

This is your Blank File Test.

You need to decide:

What data structure to use
How to represent a task
How to create the menu
How to use the loop
How to handle the user's choice
How to validate the task number
How to handle invalid menu choices

You can use the Python syntax you've already learned.

Debugging requirement 🐞

Once your application works, I will give you a deliberate bug.

You must use:

🔴 Breakpoint
▶ Continue
↻ Step Over
↓ Step Into
↑ Step Out
Variables
Call Stack
Debug Console"""


tasks = []


def add_task() -> None:
    task = input("Enter task: ")
    tasks.append({"description": task, "completed": False})

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. [{('✓' if task['completed'] else ' ')}] {task['description']}")




def complete_task():
    task_number = int(input("Enter task number: "))

    if 1 <= task_number <= len(tasks):
        tasks[task_number]["completed"] = True
        print("Task completed!")
    else:
        print("Invalid task number.")

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")




"""def complete_task():
    task_number = int(input("Enter task number: "))

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task completed!")
    else:
        print("Invalid task number.")"""