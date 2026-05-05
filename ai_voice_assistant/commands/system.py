import os
import subprocess

class SystemCommands:
    def open_app(self, app_name):
        try:
            subprocess.Popen([app_name])
            return f"Opening {app_name}."
        except Exception as e:
            return f"Could not open {app_name}. {str(e)}"

    def shutdown(self):
        os.system("shutdown /s /t 1") # Windows
        # For Linux: os.system("shutdown now")
        return "Shutting down the system."

    def restart(self):
        os.system("shutdown /r /t 1") # Windows
        # For Linux: os.system("reboot")
        return "Restarting the system."

    def get_time(self):
        import datetime
        now = datetime.datetime.now()
        return f"It is {now.strftime('%I:%M %p')}."
