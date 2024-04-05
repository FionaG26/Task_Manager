import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class ThesisTaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Thesis Task Manager")
        self.geometry("800x600")

        self.tasks = []

        self.init_ui()

    def init_ui(self):
        self.layout = tk.Frame(self)
        self.layout.pack(fill=tk.BOTH, expand=True)

        self.create_task_widgets()
        self.create_task_list_widget()

    def create_task_widgets(self):
        task_frame = tk.Frame(self.layout)
        task_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(task_frame, text="Title:").pack(anchor=tk.W)
        self.title_edit = tk.Entry(task_frame)
        self.title_edit.pack(fill=tk.X)

        tk.Label(task_frame, text="Description:").pack(anchor=tk.W)
        self.description_edit = tk.Text(task_frame, height=5)
        self.description_edit.pack(fill=tk.BOTH)

        tk.Label(task_frame, text="Category:").pack(anchor=tk.W)
        self.category_combo = ttk.Combobox(task_frame, values=['Introduction',
                                      'Literature Review',
                                      'Materials & Procedures',
                                      'Results',
                                      'Discussion',
                                      'Conclusions',
                                      'Recommendations'])
        self.category_combo.pack(fill=tk.X)

        tk.Label(task_frame, text="Priority:").pack(anchor=tk.W)
        self.priority_combo = ttk.Combobox(task_frame, values=['Low', 'Medium', 'High'])
        self.priority_combo.pack(fill=tk.X)

        tk.Label(task_frame, text="Deadline:").pack(anchor=tk.W)
        self.deadline_edit = tk.Entry(task_frame)
        self.deadline_edit.pack(fill=tk.X)

        self.add_button = tk.Button(task_frame, text="Add Task", command=self.add_task)
        self.add_button.pack()

    def create_task_list_widget(self):
        task_list_frame = tk.Frame(self.layout)
        task_list_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(task_list_frame, text="Tasks").pack(anchor=tk.W)
        self.task_list_widget = tk.Listbox(task_list_frame)
        self.task_list_widget.pack(fill=tk.BOTH, expand=True)

        self.update_task_list()

    def update_task_list(self):
        self.task_list_widget.delete(0, tk.END)
        for task in self.tasks:
            self.task_list_widget.insert(tk.END, task['title'])

    def add_task(self):
        title = self.title_edit.get()
        description = self.description_edit.get("1.0", tk.END).strip()
        category = self.category_combo.get()
        priority = self.priority_combo.get()
        deadline_str = self.deadline_edit.get()

        if title and deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Warning", "Please enter the deadline in YYYY-MM-DD format.")
                return

            self.tasks.append({'title': title,
                               'description': description,
                               'category': category,
                               'priority': priority,
                               'deadline': deadline})
            self.update_task_list()
            self.clear_task_fields()
        else:
            messagebox.showwarning("Warning", "Please fill in all required fields (title, deadline).")

    def clear_task_fields(self):
        self.title_edit.delete(0, tk.END)
        self.description_edit.delete("1.0", tk.END)
        self.category_combo.set('')
        self.priority_combo.set('')
        self.deadline_edit.delete(0, tk.END)


if __name__ == "__main__":
    app = ThesisTaskManager()
    app.mainloop()
