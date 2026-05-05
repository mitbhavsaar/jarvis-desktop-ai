# Jarvis: AI Voice Assistant

Jarvis is a powerful, multilingual AI-powered desktop assistant built with Python. It uses state-of-the-art Large Language Models (Groq Llama 3) to understand and execute your commands in English, Hindi, and Gujarati.

## 🚀 Key Features

- **Multilingual Support**: Understands and responds in English, Hindi, and Gujarati.
- **AI-Powered Intelligence**: Uses Groq (Llama 3) for lightning-fast intent extraction and conversational responses.
- **WhatsApp Automation**: Send messages to your contacts or yourself ("Me") just by speaking.
- **System Control**: Ask for the current time, open applications (Chrome, VS Code, etc.), and control your PC.
- **Smart Listening**: Works with a wake word ("Jarvis") or responds directly to strong commands (like "What is the time?").

---

## 🛠 Project Architecture

The project is organized into several modules for scalability and maintainability:

### 1. Core Engine (`core/`)
- **`main.py`**: The entry point. It runs the main loop that continuously listens for user input.
- **`listener.py`**: Handles microphone input and uses Google Speech Recognition to convert audio to text.
- **`speaker.py`**: Converts text responses back to speech using `pyttsx3`.
- **`brain.py`**: The decision-maker. It analyzes the text query to identify what you want to do.

### 2. Services (`services/`)
- **`ai_service.py`**: Connects to the Groq API. It handles conversational logic and uses AI to extract intents from complex sentences.

### 3. Commands (`commands/`)
- **`whatsapp.py`**: Uses Selenium to automate WhatsApp Web for sending messages.
- **`system.py`**: Handles local system tasks like telling the time or launching apps.
- **`tasks.py`**: (Optional) Manages your to-do list.
- **`calendar.py`**: (Optional) Integrates with Google Calendar.

### 4. Configuration & Data
- **`config.py`**: Central settings for API keys, model names, and file paths.
- **`data/contacts.json`**: A dictionary where you can save names and phone numbers for easier WhatsApp messaging.

---

## ⚙️ Setup & Installation

1. **Install Dependencies**:
   Ensure you are in your virtual environment and run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   Open [config.py](file:///home/acespritech/workspace/18.0/ai_voice_assistant/config.py) and update your Groq API Key:
   ```python
   GROQ_API_KEY = "gsk_your_actual_key_here"
   ```

3. **Prepare WhatsApp**:
   - The assistant uses a dedicated Chrome profile. 
   - On the first run of a WhatsApp command, you may need to scan the QR code to log in. It will stay logged in for future sessions.

4. **Add Contacts**:
   Add your frequently used contacts in [data/contacts.json](file:///home/acespritech/workspace/18.0/ai_voice_assistant/data/contacts.json):
   ```json
   {
     "papa": "919876543210",
     "nannu": "917000000000"
   }
   ```

---

## 🎤 How to Use

Simply run the project:
```bash
python3 main.py
```

### Example Commands:

**English:**
- "Jarvis, what is the time?"
- "Send a message to Rahul saying I will be late."
- "Open Google Chrome."

**Hindi:**
- "Jarvis, abhi kitne baje hain?"
- "Nannu ko WhatsApp par hello bolo."
- "Mera browser kholo."

**Gujarati:**
- "Ketla vagya che?"
- "Nannu ne message moklo kem cho."
- "VS Code chalao."

---

## 🛡 System Requirements
- **Python**: 3.10+
- **Chrome Browser**: Required for WhatsApp Automation.
- **ChromeDriver**: Managed automatically by the project.
- **Active Internet Connection**: Required for Speech Recognition and Groq AI.
