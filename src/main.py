import sys

# In-memory storage for tasks
tasks = []

def main_menu():
    """Displays the main menu and returns the user's choice."""
    print("\n" + "="*40)
    print("   THE EVOLUTION OF TODO (PHASE I)")
    print("="*40)
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task Details")
    print("4. Delete Task by ID")
    print("5. Mark Task as Complete/Incomplete")
    print("6. Exit")
    print("="*40)
    choice = input("\nSelect an option (1-6): ").strip()
    return choice

def add_task():
    print("\n--- ADD NEW TASK ---")
    while True:
        title = input("Enter task title: ").strip()
        if title:
            break
        print("Error: Title cannot be empty.")
    
    description = input("Enter task description (optional): ").strip()
    task_id = len(tasks) + 1
    
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    print(f"\n[Success] Task #{task_id} added.")

def view_tasks():
    print("\n--- YOUR TODO LIST ---")
    if not tasks:
        print("No tasks found.")
        return
    
    for t in tasks:
        status = "[X] Completed" if t["completed"] else "[ ] Incomplete"
        print(f"{t['id']}. {status} | Title: {t['title']}")
        if t['description']:
            print(f"   Description: {t['description']}")

def update_task():
    print("\n--- UPDATE TASK ---")
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Error: Invalid ID format.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"Error: Task #{task_id} not found.")
        return

    print(f"Updating Task #{task_id}: {task['title']}")
    new_title = input("Enter new title (leave blank to keep current): ").strip()
    new_desc = input("Enter new description (leave blank to keep current): ").strip()

    if new_title:
        task["title"] = new_title
    if new_desc:
        task["description"] = new_desc
    print(f"\n[Success] Task #{task_id} updated.")

def delete_task():
    print("\n--- DELETE TASK ---")
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Error: Invalid ID format.")
        return

    initial_length = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    
    if len(tasks) < initial_length:
        print(f"\n[Success] Task #{task_id} deleted.")
    else:
        print(f"Error: Task #{task_id} not found.")

def toggle_task():
    print("\n--- TOGGLE STATUS ---")
    try:
        task_id = int(input("Enter task ID to toggle: "))
    except ValueError:
        print("Error: Invalid ID format.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"Error: Task #{task_id} not found.")
        return

    task["completed"] = not task["completed"]
    status = "Completed" if task["completed"] else "Incomplete"
    print(f"\n[Success] Task #{task_id} is now marked as {status}.")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            toggle_task()
        elif choice == '6':
            print("\nExiting. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
