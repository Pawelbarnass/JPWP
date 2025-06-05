from datetime import datetime

class Task:
    def __init__(self):
        self.description = ""
        self.deadline = None
        self.priority = None
        self.notes = ""
        self.completed = False

    def details(self):
        parts = [self.description]
        if self.deadline:
            parts.append(f"(Due: {self.deadline.strftime('%d.%m.%Y')})")
        if self.priority:
            parts.append(f"[Priority: {self.priority}]")
        if self.completed:
            parts.append("[Completed]")
        if self.notes:
            parts.append(f"Notes: {self.notes}")
        return " ".join(parts)

class TaskBuilder:
    def __init__(self):
        self.task = Task()

    def set_description(self, desc):
        self.task.description = desc
        return self

    def set_deadline(self, deadline):
        self.task.deadline = deadline
        return self

    def set_priority(self, priority):
        self.task.priority = priority
        return self

    def set_notes(self, notes):
        self.task.notes = notes
        return self

    def build(self):
        if not self.task.description:
            raise ValueError("Description is required")
        return self.task
