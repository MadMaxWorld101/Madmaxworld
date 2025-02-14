import json

# Load Data from JSON
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"goals": {"items": []}, "todos": {"items": []}, "prompts": {"assistants": [], "tasks": []}}

data = load_data()

# 🚀 Display Main Menu
def main_menu():
    while True:
        print("\n🏆 TodaiNote Task Manager\n")
        print(" 1️⃣  Add a Goal")
        print(" 2️⃣  Add a To-Do")
        print(" 3️⃣  View Goals & To-Dos")
        print(" 4️⃣  Mark a To-Do as Complete")
        print(" 5️⃣  View AI Assistants")
        print(" 6️⃣  Exit\n")
        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            add_goal()
        elif choice == "2":
            add_todo()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            mark_todo_complete()
        elif choice == "5":
            view_assistants()
        elif choice == "6":
            print("🚪 Exiting TodaiNote...")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-6.")

# ✏️ Add a Goal
def add_goal():
    title = input("\n🎯 Enter goal title: ").strip()
    data["goals"]["items"].append({"title": title, "subtasks": []})
    print(f"✅ Goal '{title}' added!")

# ✅ Add a To-Do
def add_todo():
    task = input("\n📝 Enter To-Do: ").strip()
    data["todos"]["items"].append({"task": task, "status": "incomplete"})
    print(f"✅ To-Do '{task}' added!")

# 📂 View Goals & To-Dos
def view_tasks():
    print("\n🏆 Goals & To-Dos\n")
    
    # Display Goals
    print("## 🎯 Goals")
    for goal in data["goals"]["items"]:
        print(f"  - {goal['title']}")
        for sub in goal.get("subtasks", []):
            print(f"    - {sub['task']} [{sub['status']}]")
    
    # Display To-Dos
    print("\n## ✅ To-Dos")
    for todo in data["todos"]["items"]:
        print(f"  - {todo['task']} [{todo['status']}]")

# ✅ Mark To-Do as Complete
def mark_todo_complete():
    print("\n✅ To-Dos")
    for i, todo in enumerate(data["todos"]["items"]):
        print(f" {i + 1}. {todo['task']} [{todo['status']}]")

    try:
        choice = int(input("\n🔢 Select task number to mark complete: ")) - 1
        if 0 <= choice < len(data["todos"]["items"]):
            data["todos"]["items"][choice]["status"] = "complete"
            print("✅ Task marked as complete!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 🧠 View AI Assistants
def view_assistants():
    print("\n🧠 AI Assistants\n")
    for i, assistant in enumerate(data["prompts"]["assistants"]):
        print(f" {i + 1}. {assistant['name']} - {assistant['description']}")

    try:
        choice = int(input("\n🔢 Choose an assistant (or 0 to return): ").strip()) - 1
        if choice == -1:
            return
        elif 0 <= choice < len(data["prompts"]["assistants"]):
            interact_with_assistant(data["prompts"]["assistants"][choice])
        else:
            print("⚠️ Invalid selection.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 🎭 Interact with AI Assistant
def interact_with_assistant(assistant):
    print(f"\n🤖 {assistant['name']} - {assistant['description']}\n")

    # Display AI Tasks
    for i, task in enumerate(data["prompts"]["tasks"]):
        print(f" {i + 1}. {task['name']} - {task['details']}")

    try:
        choice = int(input("\n🔢 Choose a task (or 0 to return): ").strip()) - 1
        if choice == -1:
            return
        elif 0 <= choice < len(data["prompts"]["tasks"]):
            print(f"\n🛠️ Performing: {data['prompts']['tasks'][choice]['name']}\n")
        else:
            print("⚠️ Invalid selection.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Start the app
if __name__ == "__main__":
    main_menu()