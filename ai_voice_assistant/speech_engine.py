import speech_recognition as sr

def listen():
    """Listens to the microphone and returns the spoken text."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise briefly
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            # Listen for user input
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            print("Processing audio...")
            
            # Using Google's free speech recognition
            text = recognizer.recognize_google(audio, language="en-IN") # Can use en-IN or hi-IN depending on the user's spoken language
            print(f"You said: {text}")
            return text
            
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    result = listen()
    if result:
        print(f"Final recognized text: {result}")
