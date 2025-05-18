#import Task module
from classes.Task import *

#task manager class
class TaskManager:

    #sets _instance to none to create first singleton
    _instance = None


    #creates singleton with __new__
    def __new__(cls):
        #checks for singleton
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
        else:
            #if instance != None, pass and doesnt create new instance of class
            pass
        return cls._instance
    
    #__init__ for task list and obervers list
    def __init__(self):
        #if it has attribute tasks
        if not hasattr(self, "tasks"):
            self.tasks = []
            self.observers = []

    #function for adding tasks, using collection of inputs to build an object
    def add_tasks(self):
        print("Creating Task:")
        name_input = input("Set Task Name >> ")
        due_date_input = input("Set Due Date (e.g 01/01/2025) >> ")
        category_input = input("Set Category (e.g Home, Work) >> ")
        priority_input = input("Set Priority Level (High/Medium/Low) >> ")
        dependencies_input = input("Set Dependencies (Tasks to be completed before this task, press enter for no dependencies) >> ")
        print(" ")

        #need to keep adding to dependencies to make them usefull
        #splits a sting into a list then remakes it as a string, if it equals "" return "" as value
        dependencies_list = ", ".join(dependencies_input.split()) if dependencies_input else ""

        task = Task(
            name_input,
            due_date_input,
            category_input,
            priority_input,
            dependencies_list
        )

        #adds task object to list of tasks
        self.tasks.append(task)

        print("New Task:")
        print(f"{name_input} name: {task.name}\n{name_input} due date: {task.due_date}\n{name_input} category: {task.category}\n{name_input} priority: {task.priority}")

        #checks if printing dependencies is necessary
        if dependencies_list != "":
            print(f"{name_input} dependencies: {task.dependencies}")
        else:
            pass
        
    #function for viewing tasks, uses enumerate to transform list of objects to a list of tuples, then uses __str__ function defined in Task class to print out english readable results
    def view_tasks(self):
        #checks if there if tasks has any entries
        if not self.tasks:
            print("No tasks to display")
        else:
            print("Your tasks:")
            #loops over list tasks and keeps track of the index of each item
            for i, task in enumerate(self.tasks, 1):
                print(f"Task {i}:{task}")
        
    def mark_task_complete(self):
        task_name = input("Enter the name of the completed task: ")
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' has been completed and removed")
            else:
                print(f"No task named '{task_name}'")

    def sort_tasks(self):
        if self.category == category_input:
            print(f"{self.category}: {category_input}")
        