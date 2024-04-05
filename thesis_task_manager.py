import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QListWidget, QMessageBox,
    QLineEdit, QComboBox
)

from PyQt5.QtCore import Qt
from datetime import datetime, timedelta


class ThesisTaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thesis Task Manager")
        self.setGeometry(100, 100, 800, 600)

        self.tasks = []

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_task_widgets()
        self.create_task_list_widget()

    def create_task_widgets(self):
        self.task_widgets = QWidget()
        task_layout = QVBoxLayout()
        self.task_widgets.setLayout(task_layout)

        self.title_label = QLabel("Title:")
        self.title_edit = QLineEdit()

        self.description_label = QLabel("Description:")
        self.description_edit = QTextEdit()

        self.category_label = QLabel("Category:")
        self.category_combo = QComboBox()
        self.category_combo.addItems(['Introduction',
                                      'Literature Review',
                                      'Materials & Procedures',
                                      'Results',
                                      'Discussion',
                                      'Conclusions',
                                      'Recommendations'])

        self.priority_label = QLabel("Priority:")
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(['Low', 'Medium', 'High'])

        self.deadline_label = QLabel("Deadline:")
        self.deadline_edit = QLineEdit()

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        task_layout.addWidget(self.title_label)
        task_layout.addWidget(self.title_edit)
        task_layout.addWidget(self.description_label)
        task_layout.addWidget(self.description_edit)
        task_layout.addWidget(self.category_label)
        task_layout.addWidget(self.category_combo)
        task_layout.addWidget(self.priority_label)
        task_layout.addWidget(self.priority_combo)
        task_layout.addWidget(self.deadline_label)
        task_layout.addWidget(self.deadline_edit)
        task_layout.addWidget(self.add_button)

        self.layout.addWidget(self.task_widgets)

    def create_task_list_widget(self):
        self.task_list_widget = QListWidget()
        self.layout.addWidget(self.task_list_widget)

        self.update_task_list()

    def update_task_list(self):
        self.task_list_widget.clear()
        for task in self.tasks:
            self.task_list_widget.addItem(task['title'])

    def add_task(self):
        title = self.title_edit.text()
        description = self.description_edit.toPlainText()
        category = self.category_combo.currentText()
        priority = self.priority_combo.currentText()
        deadline_str = self.deadline_edit.text()

        if title and deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
            except ValueError:
                QMessageBox.warning(
                    self, "Warning",
                    "Please enter the deadline in YYYY-MM-DD format.")
            return

            self.tasks.append({'title': title,
                               'description': description,
                               'category': category,
                               'priority': priority,
                               'deadline': deadline})
            self.update_task_list()
            self.clear_task_fields()
        else:
            QMessageBox.warning(
                self,
                "Warning",
                "Please fill in all required fields (title, deadline).")

    def clear_task_fields(self):
        self.title_edit.clear()
        self.description_edit.clear()
        self.deadline_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThesisTaskManager()
    window.show()
    sys.exit(app.exec_())
