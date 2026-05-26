import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")
#load task from file 

def load_tasks():
    """
    loads task from json file 
    if file doesnt exist return an empty list 
    """

    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
        
    except json.JSONDecodeError:
        print("Error reading task file. ")
        return []
    
# save task to file 
def save_tasks(tasks):
    """ 
    save task into a JSON file
    """
    with open(FILE_NAME, "w") as file:
        json.dump(tasks,file, indent= 4) # this format the list to make it look professional 


def view_tasks(tasks):
    if not tasks:
        print("\n No task available. \n")
        return
    
    print("\n -------- TO DO TASKS --------")

    for index, task in enumerate(tasks, start=1): # what this does is to make sure it has indexes thats starting from 1 
        status = "Done" if task["done"] else "pending"
        print(f"{index}. {task['task']} [{status}]")
    print()

# add task 
def add_task(tasks):
    task_name = input("enter new task: ").strip()
    if not task_name:
        print("Task cannot  be empty ")
        return
        
    new_task = {
        "task": task_name,
            "done" : False
            }
    for task in tasks:
        if task["task"].lower() == task_name.lower():
            print("task already exists")
            return
    tasks.append(new_task)
    save_tasks(tasks)

    print("task added successfully. \n")

# delete task 
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("enter task number to delete: "))
        if task_number < 1 or task_number > len(tasks):
            print("invaild task number.")
            return
        confirm = input("are you sure? (y/n): ").lower()
        if confirm != 'y':
            print('delete cancelled')
            return
        deleted = tasks.pop(task_number - 1)

        save_tasks(tasks)
        print(f"Deleted task : {deleted['task']}\n")

    except ValueError:
        print("please enter a valid number.\n")

# mark task complete 
def mark_task_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("enter task number to mark as done: "))
        if task_number <1 or task_number > len(tasks):
            print("invalid task number")
            return
        tasks[task_number - 1]["completed at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("task marked as completed.\n")
    except ValueError:
        print("please enter a valid number")

# main menu 
def main():
    tasks = load_tasks()

    while True:
        print("====== TO DO LIST MENU =======")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Delete tasks")
        print("4. Mark tasks as done")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice =='5':
            print("Good bye")
            break
        else:
            print("invalid option. \n")

# run program 
if __name__ == "__main__":
    main()
        