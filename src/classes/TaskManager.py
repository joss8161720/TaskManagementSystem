#import Task module
from classes.Task import *
from classes.Logger import *

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
            self.categories = []

    #function for adding tasks, using collection of inputs to build an object
    def add_tasks(self):
        print("Creating Task:")
        name_input = input("Set Task Name >> ")
        due_date_input = input("Set Due Date (e.g 01/01/2025) >> ")
        category_input = input("Set Category (e.g Home, Work) >> ")
        priority_input = input("Set Priority Level (High/Medium/Low) >> ")
        dependencies_input = input("Set Dependencies (Tasks to be completed before this task comma seperated, press enter for no dependencies) >> ")
        print(" ")
        
        #need to keep adding to dependencies to make them usefull
        #splits a sting into a list then remakes it as a string, if it equals "" return "" as value
        dependencies = ", ".join(dependencies_input.split()) if dependencies_input else ""

        valid_dependencies = []
        if dependencies:
            dependencies_list = dependencies.split(", ")
            for dep_name in dependencies_list:
                if any(task.name == dep_name for task in self.tasks):
                    valid_dependencies.append(dep_name)
                else:
                    print(f"Error: Dependency '{dep_name}' not found. Task creation cancelled.")
                    return  # Cancel task creation if dependency is invalid

        dependencies = ", ".join(valid_dependencies)


        task = Task(
            name_input,
            due_date_input,
            category_input,
            priority_input,
            dependencies
        )

        #adds task object to list of tasks
        self.tasks.append(task)

        print("New Task:")
        print(f"{name_input} name: {task.name}\n{name_input} due date: {task.due_date}\n{name_input} category: {task.category}\n{name_input} priority: {task.priority}")

        #checks if printing dependencies is necessary
        if dependencies != "":
            print(f"{name_input} dependencies: {task.dependencies}")
        else:
            pass

        self.notify_observers(f"\nTask '{task.name}' created.\n")

        
    #function for viewing tasks, uses enumerate to transform list of objects to a list of tuples, then uses __str__ function defined in Task class to print out english readable results
    def view_tasks(self):
        #checks if there if tasks has any entries
        if not self.tasks:
            print("No tasks to display")
            return

        else:
            print("Your tasks:")
            
            #loops over list tasks and keeps track of the index of each item
            for i, task in enumerate(self.tasks, 1):
                print(f"Task {i}:{task}")
        
    def mark_task_complete(self):

        task_name = input("Enter the name of the completed task: ")

        for task in self.tasks:
            if task.name == task_name:
                
                for other_task in self.tasks:
                    if task.name in other_task.dependencies.split(", "):
                        print(f"Cannot complete '{task_name}': It is a dependency for task '{other_task.name}'.")
                        return
                
                self.tasks.remove(task)
                print(f"Task '{task_name}' has been completed and removed")
                self.notify_observers(f"\nTask '{task_name}' deleted.\n")
                return

            
        print(f"No task named '{task_name}'")


    def sort(self):
        if not self.tasks:
            print("No tasks to sort.")
            return
        
        categories = {}

        for task in self.tasks:
           
            if task.category not in categories:
                categories[task.category] = []
            categories[task.category].append(task)
        
        for category, tasks in categories.items():
            print(f"\nCategory: {category}")
            for task in tasks:
                print(f"{task}")
                

    def add_observer(self, observer):
        self.observers.append(observer)


    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)
