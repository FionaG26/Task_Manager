import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


class ThesisTaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Thesis Task Manager")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")  # Set background color

        self.tasks = []
        # Initialize layout attribute
        self.layout = tk.Frame(self, bg="#f0f0f0")

        self.title_edit = None
        self.description_edit = None
        self.category_combo = None
        self.priority_combo = None
        self.deadline_edit = None
        self.add_button = None
        self.task_list_widget = None  # Initialize task_list_widget attribute

        self.init_ui()

    def init_ui(self):
        self.layout.pack(fill=tk.BOTH, expand=True)

        self.create_task_widgets()
        self.create_task_list_widget()

    def create_task_widgets(self):
        task_frame = tk.Frame(self.layout, bg="#d9d9d9")
        task_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(
            task_frame,
            text="Title:",
            bg="#d9d9d9",
            fg="#333333").pack(
            anchor=tk.W)
        self.title_edit = tk.Entry(task_frame)
        self.title_edit.pack(fill=tk.X)

        tk.Label(
            task_frame,
            text="Description:",
            bg="#d9d9d9",
            fg="#333333").pack(
            anchor=tk.W)
        self.description_edit = tk.Text(task_frame, height=5)
        self.description_edit.pack(fill=tk.BOTH)

        tk.Label(
            task_frame,
            text="Category:",
            bg="#d9d9d9",
            fg="#333333").pack(
            anchor=tk.W)
        self.category_combo = ttk.Combobox(task_frame, values=['Introduction',
                                                               'Literature Review',
                                                               'Materials & Procedures',
                                                               'Results',
                                                               'Discussion',
                                                               'Conclusions',
                                                               'Recommendations'])
        self.category_combo.pack(fill=tk.X)

        tk.Label(
            task_frame,
            text="Priority:",
            bg="#d9d9d9",
            fg="#333333").pack(
            anchor=tk.W)
        self.priority_combo = ttk.Combobox(
            task_frame, values=['Low', 'Medium', 'High'])
        self.priority_combo.pack(fill=tk.X)

        tk.Label(
            task_frame,
            text="Deadline:",
            bg="#d9d9d9",
            fg="#333333").pack(
            anchor=tk.W)
        self.deadline_edit = tk.Entry(task_frame)
        self.deadline_edit.pack(fill=tk.X)

        self.add_button = tk.Button(
            task_frame,
            text="Add Task",
            command=self.add_task,
            bg="#4caf50",
            fg="white")
        self.add_button.pack()

    def create_task_list_widget(self):
        task_list_frame = tk.Frame(self.layout, bg="#d9d9d9")
        task_list_frame.pack(
            side=tk.RIGHT,
            padx=10,
            pady=10,
            fill=tk.BOTH,
            expand=True)

        tk.Label(
            task_list_frame,
            text="Tasks",
            bg="#d9d9d9",
            fg="#333333",
            font=(
                "Helvetica",
                12,
                "bold")).pack(
            anchor=tk.W)

        self.task_list_widget = tk.Listbox(
            task_list_frame,
            bg="white",
            selectbackground="#c3e6cb",
            selectforeground="black")
        self.task_list_widget.pack(fill=tk.BOTH, expand=True)

        self.task_list_widget.bind(
            "<Double-Button-1>",
            self.on_task_double_click)  # Bind double-click event

    def update_task_list(self):
        self.task_list_widget.delete(0, tk.END)
        for task in self.tasks:
            title = task.get('title', '')
            category = task.get('category', '')
            priority = task.get('priority', '')
            deadline = task.get('deadline', '')
            self.task_list_widget.insert(
                tk.END,
                f"Title: {title}, Category: {category}, Priority: {priority}, Deadline: {deadline}")

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
                messagebox.showwarning(
                    "Warning", "Please enter the deadline in YYYY-MM-DD format.")
                return

            self.tasks.append({'title': title,
                               'description': description,
                               'category': category,
                               'priority': priority,
                               'deadline': deadline})
            self.update_task_list()
            self.clear_task_fields()
        else:
            messagebox.showwarning(
                "Warning", "Please fill in all required fields (title, deadline).")

    def clear_task_fields(self):
        self.title_edit.delete(0, tk.END)
        self.description_edit.delete("1.0", tk.END)
        self.category_combo.set('')
        self.priority_combo.set('')
        self.deadline_edit.delete(0, tk.END)

    # Changed parameter name to underscore to indicate it's not being used
    def on_task_double_click(self, _):
        selected_index = self.task_list_widget.curselection()
        if selected_index:
            task_index = selected_index[0]
            selected_task = self.tasks[task_index]

            # Check if selected_task is a dictionary and contains the keys
            # 'title' and 'description'
            if isinstance(
                    selected_task, dict) and 'title' in selected_task and 'description' in selected_task:
                title = selected_task['title']
                description = selected_task['description']
                messagebox.showinfo(title, description)
            else:
                messagebox.showwarning("Warning", "Selected task is invalid.")


if __name__ == "__main__":
    app = ThesisTaskManager()
    app.mainloop()
