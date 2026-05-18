import time
from speech_engine import listen
from brain import get_jarvis_response
from audio_engine import speak

def main():
    print("Initializing Jarvis...")
    # Optional greeting
    speak("System initialized. I am online and ready, sir.")
    
    while True:
        # 1. Listen to user
        user_input = listen()
        
        if not user_input:
            continue
            
        # Optional exit command
        if user_input.lower() in ["exit", "quit", "stop listening", "goodbye", "bye jarvis"]:
            speak("Goodbye sir. Have a great day!")
            break
            
        # 2. Think (Send to Brain)
        print(f"Thinking...")
        response = get_jarvis_response(user_input)
        
        # 3. Speak the response
        speak(response)
        
        # Small pause before listening again
        time.sleep(0.5)

if __name__ == "__main__":
    main()
