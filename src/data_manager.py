import json
import os

# Set the data directory and JSON files
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
GOALS_FILE = os.path.join(DATA_DIR, "goals.json")
TODOS_FILE = os.path.join(DATA_DIR, "todos.json")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def load_json(file_path):
    """Loads JSON data from a file or creates an empty JSON file if missing."""
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump({"items": []}, file, indent=4)

    with open(file_path, "r") as file:
        return json.load(file)

def save_json(file_path, data):
    """Saves JSON data to a file."""
    with open(file_path, "w") as file:  # ✅ Fixed syntax error
        json.dump(data, file, indent=4)  # ✅ Corrected json.dump() usage

# Example usage
goals_data = load_json(GOALS_FILE)  # Now json is actually used!
print(goals_data)

import json
import os

# Define file paths
GOALS_FILE = "data/goals.json"
TODOS_FILE = "data/todos.json"

def load_json(filename):
    """Load JSON data from a file, return an empty structure if the file is missing."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {"items": []}  # Return an empty structure if the file doesn't exist

def save_json(filename, data):
    """Save JSON data to a file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)