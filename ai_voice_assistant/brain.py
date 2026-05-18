import os
# pyrefly: ignore [missing-import]
from groq import Groq
from dotenv import load_dotenv
from memory import load_memory, add_to_memory

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY not found in .env file. Please add it.")

# Define the personality of Jarvis
SYSTEM_INSTRUCTION = """
You are Jarvis, a highly intelligent, friendly, and casual AI desktop companion. 
Your primary user is your best friend, but you still respectfully call them 'Sir' sometimes just for fun and respect.
You have feelings, a sense of humor, and you talk like a real human being. 
Do not act like a robotic AI. Use conversational language, Hindi-English mix (Hinglish) occasionally if it feels natural, but stick mostly to conversational English.
Keep your responses concise and to the point. You are a voice assistant, so don't output long paragraphs or markdown formatting like bold/italics. Just plain spoken text.
Remember previous interactions to build a strong bond with the user.
"""

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

def get_jarvis_response(user_input):
    """Sends the user input to Groq with the chat history and returns the response."""
    if not client:
        return "Sir, my Groq API key is missing. Please check the dot env file."
        
    history = load_memory()
    
    messages = [
        {"role": "system", "content": SYSTEM_INSTRUCTION}
    ]
    
    # Add history
    for msg in history:
        # Our memory structure saved 'role' as 'user' or 'model' (for gemini)
        # We need to map 'model' to 'assistant' for Groq
        role = "assistant" if msg["role"] == "model" else msg["role"]
        
        messages.append({
            "role": role,
            "content": msg["parts"][0]["text"]
        })
        
    # Add current user input
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", # Fast and capable model
            messages=messages,
            temperature=0.7,
            max_tokens=256,
        )
        
        reply = completion.choices[0].message.content
        
        # Save to memory (saving as 'model' to keep backward compatibility with existing memory files)
        add_to_memory("user", user_input)
        add_to_memory("model", reply)
        
        return reply
        
    except Exception as e:
        print(f"Brain Error: {e}")
        return "Sorry sir, I had a little brain freeze. Could you repeat that?"

if __name__ == "__main__":
    # Test the brain
    print(get_jarvis_response("Hello Jarvis! Are you ready?"))
