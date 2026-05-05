import os
from dotenv import load_dotenv

load_dotenv()

# AI Settings (Groq)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile" # High performance model
# MODEL_NAME = "llama3-8b-8192" # Faster, lower resource model

# Assistant Settings
WAKE_WORD = "jarvis"
ASSISTANT_NAME = "Jarvis"

# WhatsApp Settings
CHROME_DRIVER_PATH = "/usr/bin/chromedriver" # Update if different
WHATSAPP_DATA_DIR = os.path.expanduser("~/.config/google-chrome/whatsapp_session")

# File Paths
DATA_DIR = "data"
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.json")

# Calendar Settings
CALENDAR_CREDENTIALS = "services/credentials.json"
CALENDAR_TOKEN = "services/token.json"
