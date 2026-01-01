import sys
import os

# ANSI Colors & Styles
BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[36m"
RED = "\033[31m"
YELLOW = "\033[33m"

# In-memory storage for tasks
tasks = []

def main_menu():
    """Displays the main menu and returns the user's choice."""
    # Clear screen for a cleaner feel (optional, but nice)
    # os.system('cls' if os.name == 'nt' else 'clear') 
    
    print("\n" + CYAN + "="*50 + RESET)
    print(f"   {BOLD}THE EVOLUTION OF TODO (PHASE I){RESET}")
    print(CYAN + "="*50 + RESET)
    print(f"{GREEN}1.{RESET} {BOLD}Add Task{RESET}")
    print(f"{GREEN}2.{RESET} {BOLD}View Task List{RESET}")
    print(f"{GREEN}3.{RESET} {BOLD}Update Task Details{RESET}")
    print(f"{GREEN}4.{RESET} {BOLD}Delete Task by ID{RESET}")
    print(f"{GREEN}5.{RESET} {BOLD}Mark Task as Complete/Incomplete{RESET}")
    print(f"{RED}6.{RESET} {BOLD}Exit{RESET}")
    print(CYAN + "="*50 + RESET)
    
    choice = input(f"\n{BOLD}Select an option {CYAN}➜{RESET} ").strip()
    return choice

def add_task():
    print(f"\n{YELLOW}--- ADD NEW TASK ---{RESET}")
    while True:
        title = input(f"Enter task title {BOLD}➜{RESET} ").strip()
        if title:
            break
        print(f"{RED}Error: Title cannot be empty.{RESET}")
    
    description = input(f"Enter task description (optional) {BOLD}➜{RESET} ").strip()
    task_id = len(tasks) + 1
    
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    print(f"\n{GREEN}[Success] Task #{task_id} added.{RESET}")

def view_tasks():
    print(f"\n{YELLOW}--- YOUR TODO LIST ---{RESET}")
    if not tasks:
        print("No tasks found.")
        return
    
    for t in tasks:
        # Fancy Checkbox
        status_icon = f"{GREEN}✔{RESET}" if t["completed"] else f"{RED}✖{RESET}"
        status_text = f"{GREEN}Completed{RESET}" if t["completed"] else f"{RED}Incomplete{RESET}"
        
        print(f"{BOLD}{t['id']}.{RESET} [{status_icon}] {status_text} | {BOLD}{t['title']}{RESET}")
        if t['description']:
            print(f"   Description: {t['description']}")

def update_task():
    print(f"\n{YELLOW}--- UPDATE TASK ---{RESET}")
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print(f"{RED}Error: Invalid ID format.{RESET}")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"{RED}Error: Task #{task_id} not found.{RESET}")
        return

    print(f"Updating Task #{task_id}: {BOLD}{task['title']}{RESET}")
    new_title = input(f"Enter new title (leave blank to keep current): ").strip()
    new_desc = input(f"Enter new description (leave blank to keep current): ").strip()

    if new_title:
        task["title"] = new_title
    if new_desc:
        task["description"] = new_desc
    print(f"\n{GREEN}[Success] Task #{task_id} updated.{RESET}")

def delete_task():
    print(f"\n{YELLOW}--- DELETE TASK ---{RESET}")
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print(f"{RED}Error: Invalid ID format.{RESET}")
        return

    initial_length = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    
    if len(tasks) < initial_length:
        print(f"\n{GREEN}[Success] Task #{task_id} deleted.{RESET}")
    else:
        print(f"{RED}Error: Task #{task_id} not found.{RESET}")

def toggle_task():
    print(f"\n{YELLOW}--- TOGGLE STATUS ---{RESET}")
    try:
        task_id = int(input("Enter task ID to toggle: "))
    except ValueError:
        print(f"{RED}Error: Invalid ID format.{RESET}")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"{RED}Error: Task #{task_id} not found.{RESET}")
        return

    task["completed"] = not task["completed"]
    status = "Completed" if task["completed"] else "Incomplete"
    print(f"\n{GREEN}[Success] Task #{task_id} is now marked as {status}.{RESET}")

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
            print(f"\n{CYAN}Exiting. Goodbye!{RESET}")
            sys.exit(0)
        else:
            print(f"\n{RED}Invalid choice. Please select 1-6.{RESET}")

if __name__ == "__main__":
    main()
