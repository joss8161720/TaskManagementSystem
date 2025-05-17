from Task import *


class TaskManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating singleton intance")
            cls._instance = super(TaskManager, cls).__new__(cls)
        else:
            print("Loading an existing instance")
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "tasks"):
            self.tasks = []
            self.observers = []

    def add_tasks(self):
        print("Creating Task")
        name_input = input("Set Task Name: ")
        due_date_input = input("Set Due Date (e.g 01/01/2025): ")
        category_input = input("Set Category: ")
        priority_input = input("Set Priority Level (High/Medium/Low): ")
        dependencies_input = input("Set Dependencies (Tasks to be completed before this task, press enter for no dependencies): ")

        dependencies_list = dependencies_input.split(" ")

        
        task = Task(
            name_input,
            due_date_input,
            category_input,
            priority_input,
            False,
            dependencies_list
        )

        self.tasks.append(task)

        print(f"Task name: {task.name}\nTask due date: {task.due_date}\nTask category: {task.category}\nTask priority: {task.priority}\nTask dependencies: {task.dependencies}")

        

        
