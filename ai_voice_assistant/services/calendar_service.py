import os.path
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import config

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class CalendarService:
    def get_service(self):
        creds = None
        if os.path.exists(config.CALENDAR_TOKEN):
            creds = Credentials.from_authorized_user_file(config.CALENDAR_TOKEN, SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(config.CALENDAR_CREDENTIALS, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(config.CALENDAR_TOKEN, 'w') as token:
                token.write(creds.to_json())

        return build('calendar', 'v3', credentials=creds)

    def get_upcoming_events(self, max_results=10):
        service = self.get_service()
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=max_results, singleEvents=True,
                                              orderBy='startTime').execute()
        return events_result.get('items', [])
