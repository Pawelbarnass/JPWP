class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def list_tasks(self):
        for i, t in enumerate(self.tasks):
            status = "✓" if t.completed else "✗"
            print(f"{i}. [{status}] {t.details()}")
