class Task:
    def __init__(self, title, due_date, category, priority, dependencies=None):
        self.title = title
        self.due_date = due_date  # stored as string, e.g. "2025-05-14"
        self.category = category
        self.priority = priority  # e.g., 'High', 'Medium', 'Low'
        self.dependencies = dependencies if dependencies else []
        self.completed = False

    def can_complete(self):
        return all(dep.completed for dep in self.dependencies)

    def mark_complete(self):

        if self.can_complete():

            self.completed = True
            print(f"Task '{self.title}' marked as complete.")

        else:
            print(f"Cannot complete '{self.title}'. Dependencies incomplete.")

    def __str__(self):
        dep_titles = [dep.title for dep in self.dependencies]
        return f"Title: {self.title} | Due: {self.due_date} | Category: {self.category} | Priority: {self.priority} | Complete: {self.completed} | Depends on: {dep_titles}"

class TaskManager:
    def __init__(self):

        self.tasks = []

    def find_task(self, title):

        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def add_task(self, title, due_date, category, priority, dependency_titles):

        dependencies = []

        for dep_title in dependency_titles:
            dep_task = self.find_task(dep_title)
            if dep_task:
                dependencies.append(dep_task)
            else:
                print(f"Warning: Dependency '{dep_title}' not found. Skipping.")

        new_task = Task(title, due_date, category, priority, dependencies)
        self.tasks.append(new_task)
        print(f"Task '{title}' added.")

    def view_tasks(self):

        if not self.tasks:
            print("No tasks available.")
            return
        
        for task in self.tasks:
            print(task)

    def mark_task_complete(self, task_title):

        task = self.find_task(task_title)
        
        if task:
            task.mark_complete()
        else:
            print("Task not found.")

def main():

    manager = TaskManager()

    while True:

        print("\nOptions: add, view, complete, quit")

        action = input("Choose action: ").strip().lower()

        if action == "add":
            title = input("Task title: ").strip()
            due_date = input("Due date (e.g. 2025-05-14): ").strip()
            category = input("Category: ").strip()
            priority = input("Priority (High/Medium/Low): ").strip()
            dep_input = input("Dependencies (comma-separated titles, or leave blank): ").strip()
            dependency_titles = [d.strip() for d in dep_input.split(",") if d.strip()] if dep_input else []
            manager.add_task(title, due_date, category, priority, dependency_titles)

        elif action == "view":
            manager.view_tasks()

        elif action == "complete":
            title = input("Enter task title to complete: ").strip()
            manager.mark_task_complete(title)

        elif action == "quit":
            print("Goodbye!")
            break

        else:

            print("Invalid option.")

main()
