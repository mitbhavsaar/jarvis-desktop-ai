from services.calendar_service import CalendarService

class CalendarCommands:
    def __init__(self):
        self.service = CalendarService()

    def get_today_events(self):
        try:
            events = self.service.get_upcoming_events(max_results=5)
            if not events:
                return "No upcoming events found."
            
            res = "You have the following meetings: "
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                res += f"{event['summary']} at {start}. "
            return res
        except Exception as e:
            return f"Error fetching calendar: {str(e)}"
