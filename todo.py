import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty list if the file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
        
def view_tasks(tasks):
    """Displays all current tasks in a numbered list."""
    print("\n--- 📝 Your To-Do List ---")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
    print("--------------------------\n")

def add_task(tasks):
    """Prompts the user for a new task and adds it to the list."""
    new_task = input("Enter the new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Task '{new_task}' added.")
def delete_task(tasks):
    """Deletes a task from the list based on its number."""
    view_tasks(tasks)
    if not tasks:
        return
        
    try:
        task_num_to_delete = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num_to_delete <= len(tasks):
            removed_task = tasks.pop(task_num_to_delete - 1)
            save_tasks(tasks)
            print(f"🗑️  Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the to-do list application loop."""
    tasks = load_tasks()
    
    print("🗒️  Welcome to your Simple To-Do List! 🗒️")
    
    while True:
        print("\nWhat would you like to do?")
        print("  1. View tasks")
        print("  2. Add a task")
        print("  3. Delete a task")
        print("  4. Quit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# --- Main execution block ---
if __name__ == "__main__":
    main()
