from typing import List

# Observer pattern components
class TaskObserver:
    def notify(self, task):
        pass

class Logger(TaskObserver):
    def notify(self, task):
        print(f"[Logger] Notification: Task '{task.title}' completed.")

# Singleton TaskManager
class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def __init__(self):
        # observers only initialized once
        if not hasattr(self, 'observers'):
            self.observers: List[TaskObserver] = []

    def register_observer(self, observer: TaskObserver):
        self.observers.append(observer)

    def notify_observers(self, task):
        for obs in self.observers:
            obs.notify(task)

    def find_task(self, title):
        return next((task for task in self.tasks if task.title == title), None)

    def add_task(self, title, due_date, category, priority, dependency_titles):
        dependencies = []
        for dep_title in dependency_titles:
            dep = self.find_task(dep_title)
            if dep:
                dependencies.append(dep)
            else:
                print(f"Warning: Dependency '{dep_title}' not found.")
        new_task = Task(title, due_date, category, priority, dependencies)
        self.tasks.append(new_task)
        print(f"Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def mark_task_complete(self, task_title):
        task = self.find_task(task_title)
        if task:
            if task.mark_complete():
                self.notify_observers(task)
        else:
            print("Task not found.")

# Task class with no changes to logic but mark_complete returns success status
class Task:
    def __init__(self, title, due_date, category, priority, dependencies=None):
        self.title = title
        self.due_date = due_date
        self.category = category
        self.priority = priority
        self.dependencies = dependencies if dependencies else []
        self.completed = False

    def can_complete(self):
        return all(dep.completed for dep in self.dependencies)

    def mark_complete(self):
        if self.can_complete():
            self.completed = True
            print(f"Task '{self.title}' marked as complete.")
            return True
        else:
            print(f"Cannot complete '{self.title}'. Dependencies incomplete.")
            return False

    def __str__(self):
        dep_titles = [dep.title for dep in self.dependencies]
        return f"Title: {self.title} | Due: {self.due_date} | Category: {self.category} | Priority: {self.priority} | Complete: {self.completed} | Depends on: {dep_titles}"

# Facade pattern
class TaskApp:
    def __init__(self):
        self.manager = TaskManager()
        self.manager.register_observer(Logger())

    def run(self):
        while True:
            print("\nOptions: add, view, complete, quit")
            action = input("Choose action: ").strip().lower()

            if action == "add":
                title = input("Task title: ").strip()
                due_date = input("Due date (e.g. 2025-05-14): ").strip()
                category = input("Category: ").strip()
                priority = input("Priority (High/Medium/Low): ").strip()
                dep_input = input("Dependencies (comma-separated): ").strip()
                deps = [d.strip() for d in dep_input.split(",") if d.strip()] if dep_input else []
                self.manager.add_task(title, due_date, category, priority, deps)

            elif action == "view":
                self.manager.view_tasks()

            elif action == "complete":
                title = input("Enter task title to complete: ").strip()
                self.manager.mark_task_complete(title)

            elif action == "quit":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    app = TaskApp()
    app.run()
