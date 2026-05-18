import json
import os

MEMORY_FILE = "jarvis_memory.json"

def load_memory():
    """Loads the memory from a JSON file."""
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading memory: {e}")
            return []
    return []

def save_memory(history):
    """Saves the conversation history to a JSON file."""
    try:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        print(f"Error saving memory: {e}")

def add_to_memory(role, text):
    """Adds a new message to the memory and keeps only the last N turns to avoid context overflow."""
    history = load_memory()
    history.append({"role": role, "parts": [{"text": text}]})
    
    # Keep the last 20 messages (10 turns) to prevent the context from getting too large
    if len(history) > 20:
        history = history[-20:]
        
    save_memory(history)
