import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from task_builder import TaskBuilder

class TaskForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Task")
        self.geometry("400x350")
        self.resizable(False, False)
        self.result = None  # Will store the TaskBuilder or None if cancelled

        self.create_widgets()
        self.grab_set()

    def create_widgets(self):
        pad = {'padx': 10, 'pady': 5}

        # Opis (wymagane)
        ttk.Label(self, text="Description *").grid(row=0, column=0, sticky=tk.W, **pad)
        self.desc_entry = ttk.Entry(self, width=40)
        self.desc_entry.grid(row=0, column=1, **pad)

        # Deadline)
        ttk.Label(self, text="Deadline (DD-MM-YYYY)").grid(row=1, column=0, sticky=tk.W, **pad)
        self.deadline_entry = ttk.Entry(self, width=20)
        self.deadline_entry.grid(row=1, column=1, **pad)

        # Priorytet
        ttk.Label(self, text="Priority").grid(row=3, column=0, sticky=tk.W, **pad)
        self.priority_entry = ttk.Entry(self, width=20)
        self.priority_entry.grid(row=3, column=1, **pad)

        # Notatki
        ttk.Label(self, text="Notes").grid(row=4, column=0, sticky=tk.NW, **pad)
        self.notes_text = tk.Text(self, width=30, height=5)
        self.notes_text.grid(row=4, column=1, **pad)

        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=15)

        ttk.Button(btn_frame, text="Add Task", command=self.on_add).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.on_cancel).pack(side=tk.LEFT, padx=5)

    def on_add(self):
        desc = self.desc_entry.get().strip()
        if not desc:
            messagebox.showerror("Error", "Description is required.")
            return

        builder = TaskBuilder().set_description(desc)

        deadline_str = self.deadline_entry.get().strip()
        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, "%d.%m.%Y")
                builder.set_deadline(deadline)
            except ValueError:
                messagebox.showerror("Error", "Deadline must be DD.MM.YYY format.")
                return

        recurring_str = self.recurring_entry.get().strip()
        if recurring_str:
            if recurring_str.isdigit():
                builder.set_recurring_interval(int(recurring_str))
            else:
                messagebox.showerror("Error", "Recurring interval must be an integer.")
                return

        priority = self.priority_entry.get().strip()
        if priority:
            builder.set_priority(priority)

        notes = self.notes_text.get("1.0", tk.END).strip()
        if notes:
            builder.set_notes(notes)

        self.result = builder.build()
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()
