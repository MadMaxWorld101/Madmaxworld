import json
import os

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
PROMPTS_FILE = os.path.join(DATA_DIR, "prompts.json")

def load_prompts():
    """Load prompts from the JSON file."""
    if not os.path.exists(PROMPTS_FILE):
        print("Error: prompts.json not found.")
        return {}

    with open(PROMPTS_FILE, "r") as file:
        return json.load(file)

def pick_assistant():
    """Let the user choose an assistant."""
    prompts = load_prompts()
    if not prompts:
        return

    assistants = list(prompts["assistants"].keys())

    print("\nPick an Assistant:")
    for i, assistant in enumerate(assistants, 1):
        print(f"{i}. {assistant}")

    choice = input("\nSelect an assistant (number): ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(assistants):
        selected = assistants[int(choice) - 1]
        print(f"\nYou selected: {selected}")
        print(f"Description: {prompts['assistants'][selected]['description']}\n")
        pick_task(selected, prompts)
    else:
        print("\nInvalid selection. Try again.")

def pick_task(assistant, prompts):
    """Let the user choose a task for the selected assistant."""
    tasks = prompts["assistants"][assistant]["tasks"]

    print("\nAvailable Tasks:")
    task_list = list(tasks.keys())
    
    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task}")

    choice = input("\nSelect a task (number): ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(task_list):
        selected_task = task_list[int(choice) - 1]
        show_full_prompt(assistant, selected_task, tasks[selected_task])
    else:
        print("\nInvalid selection. Try again.")

def show_full_prompt(assistant, task, task_description):
    """Display the full prompt as a single block for easy copying."""
    print("\n--- Full Prompt ---")
    prompt_text = f"""
Assistant: {assistant}
Task: {task}
Description: {task_description}
"""
    print(prompt_text)
    print("Copy and paste this prompt for easy use.")

if __name__ == "__main__":
    pick_assistant()