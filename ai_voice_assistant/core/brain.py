import re
from commands.system import SystemCommands
from commands.whatsapp import WhatsAppCommands
from commands.tasks import TaskManager
from commands.calendar import CalendarCommands
from services.ai_service import AIService

class Brain:
    def __init__(self):
        self.ai = AIService()
        self.system = SystemCommands()
        self.whatsapp = WhatsAppCommands()
        self.tasks = TaskManager()
        self.calendar = CalendarCommands()

    def process_command(self, query):
        if not query:
            return "I didn't hear anything."

        # 1. Quick Keyword Check (for performance)
        if any(word in query for word in ["time", "baje", "samay", "vagya"]):
            return self.system.get_time()

        # 2. Advanced Intent Extraction via LLM
        print(f"Analyzing intent for: {query}")
        result = self.ai.extract_intent(query)
        intent = result.get("intent")
        params = result.get("params", {})

        if intent == "whatsapp_send":
            contact = params.get("contact")
            message = params.get("message")
            if contact and message:
                return self.whatsapp.send_message(contact, message)
            return "I understood you want to send a WhatsApp, but couldn't get the contact or message."

        elif intent == "time_query":
            return self.system.get_time()

        elif intent == "open_app":
            app = params.get("app_name", "").lower()
            if "chrome" in app:
                return self.system.open_app("google-chrome")
            if "code" in app:
                return self.system.open_app("code")
            return self.system.open_app(app)

        # 3. Fallback to general AI conversation
        return self.ai.get_response(query)
