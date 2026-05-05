import time
import config
from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain
from utils.helpers import get_greeting, clean_query

def main():
    listener = Listener()
    speaker = Speaker()
    brain = Brain()

    greeting = get_greeting()
    speaker.speak(f"{greeting}")

    while True:
        # Step 1: Listen for Command
        query = listener.listen()
        
        if not query:
            continue

        # Step 2: Decide if we should process
        wake_words = [config.WAKE_WORD.lower(), "germs", "service", "garvis", "charvis"]
        is_wake_word_present = any(w in query.lower() for w in wake_words)
        
        # Check for direct strong commands even without wake word
        # (e.g., "abhi kitne baje hai", "send message to...")
        direct_commands = ["time", "baje", "samay", "vagya", "whatsapp", "message", "moklo", "bhejo", "open", "kholo"]
        is_direct_command = any(word in query.lower() for word in direct_commands)

        if is_wake_word_present or is_direct_command:
            command = clean_query(query)
            
            # If it's just "Jarvis", ask for command
            if not command and is_wake_word_present:
                speaker.speak("Yes? I'm listening.")
                command = listener.listen()
            
            if command:
                if "exit" in command or "stop" in command or "bye" in command:
                    speaker.speak("Goodbye!")
                    break
                
                # Step 3: Process via Brain
                response = brain.process_command(command)
                
                # Step 4: Speak Response
                speaker.speak(response)

if __name__ == "__main__":
    main()
