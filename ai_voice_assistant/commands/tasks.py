import json
import os
import config

class TaskManager:
    def __init__(self):
        self.tasks_file = config.TASKS_FILE
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(config.DATA_DIR):
            os.makedirs(config.DATA_DIR)
        if not os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'w') as f:
                json.dump([], f)

    def add_task(self, query):
        # Simplistic extraction: "yaad dilana meeting at 10" -> "meeting at 10"
        task = query.replace("yaad dilana", "").replace("remind me to", "").strip()
        with open(self.tasks_file, 'r') as f:
            tasks = json.load(f)
        tasks.append(task)
        with open(self.tasks_file, 'w') as f:
            json.dump(tasks, f)
        return f"Task added: {task}"

    def list_tasks(self):
        with open(self.tasks_file, 'r') as f:
            tasks = json.load(f)
        if not tasks:
            return "You have no tasks."
        return "Your tasks are: " + ", ".join(tasks)
