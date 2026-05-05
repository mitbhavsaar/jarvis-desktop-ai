from groq import Groq
import config

class AIService:
    def __init__(self):
        self.client = Groq(api_key=config.GROQ_API_KEY)
        self.history = [{"role": "system", "content": "You are Jarvis, a helpful desktop assistant. You understand English, Hindi, and Gujarati. Always respond in the same language the user speaks to you. Keep responses brief and conversational."}]

    def get_response(self, prompt):
        self.history.append({"role": "user", "content": prompt})
        try:
            response = self.client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=self.history
            )
            reply = response.choices[0].message.content
            self.history.append({"role": "assistant", "content": reply})
            
            # Keep history short (last 10 messages)
            if len(self.history) > 11:
                self.history = [self.history[0]] + self.history[-10:]
                
            return reply
        except Exception as e:
            return f"I'm having trouble connecting to my brain. Error: {str(e)}"

    def extract_intent(self, query):
        system_prompt = """
        You are an intent extractor for a desktop assistant. 
        Analyze the user query and return ONLY a JSON object with 'intent' and 'params'.
        Languages: English, Hindi, Gujarati.
        Intents:
        - 'whatsapp_send': params={'contact': str, 'message': str}
        - 'time_query': params={}
        - 'open_app': params={'app_name': str}
        - 'unknown': params={}

        Examples:
        "Nannu ko whatsapp mein hello bolo" -> {"intent": "whatsapp_send", "params": {"contact": "Nannu", "message": "hello"}}
        "abhi kitne baje hai" -> {"intent": "time_query", "params": {}}
        "open chrome" -> {"intent": "open_app", "params": {"app_name": "chrome"}}
        """
        try:
            response = self.client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                response_format={"type": "json_object"}
            )
            import json
            return json.loads(response.choices[0].message.content)
        except Exception:
            return {"intent": "unknown", "params": {}}
