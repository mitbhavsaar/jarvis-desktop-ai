import speech_recognition as sr

class Listener:
    def __init__(self, language='en-IN'):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        # Improvements for better sensitivity
        self.recognizer.pause_threshold = 1.0  # More time for the user to complete a sentence
        self.recognizer.energy_threshold = 300  # Minimum audio energy to consider for recording
        self.recognizer.dynamic_energy_threshold = True

    def listen(self, prompt=None):
        with self.microphone as source:
            if prompt:
                print(prompt)
            # Adjust only for a very short duration to avoid missing speech
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            try:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
                print("Recognizing...")
                # en-IN is good for mixed Indian languages. 
                # For pure Hindi use 'hi-IN', for Gujarati use 'gu-IN'
                query = self.recognizer.recognize_google(audio, language=self.language)
                print(f"User: {query}")
                return query.lower()
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                print("Network error.")
                return ""
            except Exception:
                return ""
