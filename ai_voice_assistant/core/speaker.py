import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        # On Ubuntu, usually voice[0] is male, voice[11] is something else. 
        # Selecting a decent one if available.
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 180) # Speed of speech

    def speak(self, text):
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    s = Speaker()
    s.speak("Hello, I am Jarvis. How can I help you today?")
