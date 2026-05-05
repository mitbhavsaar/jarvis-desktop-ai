import datetime

def get_greeting():
    return "Hello Mit"

def clean_query(query):
    # Remove wake word variations
    wake_words = ["jarvis", "germs", "service", "garvis", "charvis"]
    query = query.lower()
    for w in wake_words:
        query = query.replace(w, "")
    return query.strip()
