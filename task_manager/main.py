import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
from task_manager import TaskManager
from task_creation_form import TaskForm

class TaskManagerUI:
    def __init__(self, root):
        self.root = root
        self.tm = TaskManager()
        self.root.title("Task Manager")
        self.root.geometry("600x400")

        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(self.frame, text="Personal Task Manager", font=("Helvetica", 16, "bold"))
        title.pack(pady=(0,10))

        self.listbox = tk.Listbox(self.frame, width=60, height=15, font=("Helvetica", 12))
        self.listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Complete Task", command=self.complete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.refresh).pack(side=tk.LEFT, padx=5)

        self.refresh()

    def add_task(self):
        form = TaskForm(self.root)
        self.root.wait_window(form)

        task = form.result
        if task:
            self.tm.add_task(task)
            self.refresh()


    def complete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to complete")
            return
        idx = selected[0]
        self.tm.complete_task(idx)
        self.refresh()

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to delete")
            return
        idx = selected[0]
        self.tm.delete_task(idx)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        now = datetime.now().date()

        for i, t in enumerate(self.tm.tasks):
            status = "✓" if t.completed else "✗"
            display_text = f"{i}. [{status}] {t.details()}"
            self.listbox.insert(tk.END, display_text)

            if t.deadline and not t.completed:
                if t.deadline.date() <= now:
                    self.listbox.itemconfig(i, bg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.mainloop()
