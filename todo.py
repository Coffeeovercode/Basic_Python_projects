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
