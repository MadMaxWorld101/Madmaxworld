import json
import os
import subprocess

# Set data directory and files
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
GOALS_FILE = os.path.join(DATA_DIR, "goals.json")
TODOS_FILE = os.path.join(DATA_DIR, "todos.json")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def load_json(file_path):
    """Loads JSON data from a file or creates a default empty structure if missing or empty."""
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        data = {"items": []}
        save_json(file_path, data)
        return data

    with open(file_path, "r") as file:
        return json.load(file)

def save_json(file_path, data):
    """Saves JSON data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def add_goal():
    """Prompts the user for a goal and its subtasks."""
    title = input("\n📌 Enter goal title: ").strip()
    subtasks = []

    # Add subtasks
    while True:
        subtask = input("  ➜ Enter subtask (or leave empty to finish): ").strip()
        if not subtask:
            break
        # Each subtask is initialized with a "status" key
        subtasks.append({"task": subtask, "status": "[ ]"})

    # Ensure the goal always has the 'subtasks' key
    goal = {"title": title, "subtasks": subtasks}

    # Load existing goals, add new goal
    goals = load_json(GOALS_FILE)
    goals["items"].append(goal)
    save_json(GOALS_FILE, goals)
    print(f"✅ Goal '{title}' added successfully!\n")

def add_to_do():
    to_do_item = input("📝 Enter to-do item: ")
    todos = load_json(TODOS_FILE)  # Load current To-Dos
    todos["items"].append({"task": to_do_item, "status": "[ ]"})  # Add new To-Do with status
    save_json(TODOS_FILE, todos)  # Save updated list of To-Dos to the JSON file
    print(f"✅ To-Do '{to_do_item}' added successfully!")

def view_data():
    goals = load_json(GOALS_FILE)  # Load goals
    todos = load_json(TODOS_FILE)  # Load to-dos
    markdown = "# Goals & To-Dos\n\n"

    # Display Goals
    for goal in goals["items"]:
        markdown += f"### Goal: {goal['title']}\n"
        for subtask in goal.get("subtasks", []):  # Safe access to subtasks, even if it's missing
            status = subtask.get('status', '[ ]')  # Default to '[ ]' if 'status' key is missing
            markdown += f"  - {status} {subtask.get('task', 'Unknown Task')}\n"

    # Display To-Dos
    markdown += "\n### To-Dos\n"
    for todo in todos["items"]:
        markdown += f"  - {todo['status']} {todo['task']}\n"  # Showing 'status' and 'task'

    print(markdown)  # Output the markdown formatted list

    subprocess.run(["glow", "-"], input=markdown, text=True)

def display_menu():
    """Displays the main menu using 'glow'."""
    menu_text = """
# 🏆 TodaiNote Task Manager

**Choose an option:**
1️⃣  Add a Goal
2️⃣  Add a To-Do
3️⃣  View Goals & To-Dos
4️⃣  Exit

👉 Enter your choice: 
"""
    subprocess.run(["glow", "-"], input=menu_text, text=True)

def main():
    """Handles user input in a loop."""
    while True:
        display_menu()
        choice = input().strip()

        if choice == "1":
            add_goal()
        elif choice == "2":
            add_to_do()
        elif choice == "3":
            view_data()
        elif choice == "4":
            print("\n👋 Exiting TodaiNote. See you next time!\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()