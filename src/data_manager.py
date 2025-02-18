import json
import os

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
DATA_FILE = os.path.join(DATA_DIR, "data.json")
ASSISTANTS_FILE = os.path.join(DATA_DIR, "assistants.json")

# Load JSON Data
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"goals": {"items": []}, "todos": {"items": []}, "prompts": {"assistants": [], "tasks": []}}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Load AI Assistants
def load_assistants():
    try:
        with open(ASSISTANTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"assistants": {}}

# Add Goal
def add_goal(data):
    """Add a new goal to the data."""
    goal = input("Enter a new goal: ").strip()
    if goal:
        data["goals"]["items"].append({"goal": goal, "completed": False})

# Add To-Do
def add_todo(data):
    """Add a new to-do to the data."""
    todo = input("Enter a new to-do: ").strip()
    if todo:
        data["todos"]["items"].append({"todo": todo, "completed": False})

# Mark To-Do as Complete
def mark_todo_complete(data):
    """Mark a to-do as complete."""
    todo_index = int(input("Enter the index of the to-do to mark as complete: "))
    if 0 <= todo_index < len(data["todos"]["items"]):
        data["todos"]["items"][todo_index]["completed"] = True
    else:
        print("Invalid index.")

# View Tasks
def view_tasks(data):
    """View all goals and to-dos."""
    print("\nGoals:")
    for i, goal in enumerate(data["goals"]["items"]):
        print(f"{i}. {goal['goal']} (Completed: {goal['completed']})")
    
    print("\nTo-Dos:")
    for i, todo in enumerate(data["todos"]["items"]):
        print(f"{i}. {todo['todo']} (Completed: {todo['completed']})")

# Main Execution
if __name__ == "__main__":
    data = load_data()
    assistants = load_assistants()

    # Menu or User Interaction Logic
    while True:
        action = input("\nChoose an action: [1] Add Goal [2] Add To-Do [3] View Tasks [4] Mark To-Do Complete [5] Save & Exit: ").strip()
        
        if action == "1":
            add_goal(data)
        elif action == "2":
            add_todo(data)
        elif action == "3":
            view_tasks(data)
        elif action == "4":
            mark_todo_complete(data)
        elif action == "5":
            save_data(data)
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid option, try again.")