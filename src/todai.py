from data_manager import load_data, save_data, add_goal, add_todo, view_tasks, mark_todo_complete
import prompt_menu
import json

# Load Data
data = load_data()

# Main Menu
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
            add_goal(data)  # Pass 'data'
        elif choice == "2":
            add_todo(data)  # Pass 'data'
        elif choice == "3":
            view_tasks(data)  # Pass 'data'
        elif choice == "4":
            mark_todo_complete(data)  # Pass 'data'
        elif choice == "5":
            print (prompt_menu.pick_assistant())
        elif choice == "6":
            print("🚪 Exiting TodaiNote...")
            save_data(data)  # Save before exiting
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-6.")

# Start the App
if __name__ == "__main__":
    main_menu()