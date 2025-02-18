import json
from data_manager import load_assistants

# Load AI Assistants
prompts = load_assistants()
assistants = prompts.get("assistants", {})  # Extract assistants safely

def pick_assistant():
    """Let the user choose an assistant."""
    
    if not assistants:
        print("No assistants found.")
        return

    while True:
        print("\nAvailable Assistants:")
        for i, assistant in enumerate(assistants.keys(), 1):
            print(f"{i}. {assistant}")

        choice = input("\nSelect an assistant (number or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting assistant selection.")
            break

        if choice.isdigit() and 1 <= int(choice) <= len(assistants):
            selected = list(assistants.keys())[int(choice) - 1]
            print(f"\nYou selected: {selected}")
            print(f"Description: {assistants[selected].get('description', 'No description available.')}\n")
        else:
            print("\nInvalid selection. Please enter a valid number or 'q' to quit.")