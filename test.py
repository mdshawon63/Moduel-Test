import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    
    print("--- Add New Task ---")
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return
    
    description = input("Enter task description: ").strip()
    
    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Invalid priority! Please choose High, Medium, or Low.")
    
    task = {
        "title": title,
        "description": description,
        "priority": priority
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    
    print("\n" + "="*50)
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['title']} - {task['description']} [{task['priority']} Priority]")
    print("="*50)

def delete_task(tasks):
    """Delete a task by its number"""
    if not tasks:
        print("\nNo tasks to delete!")
        return
    
    view_tasks(tasks)
    
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def update_task_priority(tasks):
    """Update the priority of an existing task"""
    if not tasks:
        print("\nNo tasks to update!")
        return
    
    view_tasks(tasks)
    
    try:
        task_num = int(input("\nEnter task number to update priority: "))
        if 1 <= task_num <= len(tasks):
            while True:
                new_priority = input("Enter new priority (High/Medium/Low): ").strip().capitalize()
                if new_priority in ["High", "Medium", "Low"]:
                    tasks[task_num - 1]["priority"] = new_priority
                    save_tasks(tasks)
                    print("Task priority updated successfully!")
                    break
                print("Invalid priority! Please choose High, Medium, or Low.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program loop"""
    tasks = load_tasks()
    
    while True:
        print("\n" + "="*30)
        print("===== Task Tracker =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task Priority")
        print("5. Exit")
        print("="*30)
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            update_task_priority(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
