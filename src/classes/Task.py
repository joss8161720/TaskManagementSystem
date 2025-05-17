class Task:
    #__init__ to define what a task needs
    def __init__(self,name, due_date, category, priority, completed, dependencies):
        self.name = name 
        self.due_date = due_date
        self.category = category
        self.priority = priority
        self.completed = False
        self.dependencies = dependencies

    #for updading for it has been completed
    def status(self):
        if self.completed == False:
            print("Task is not completed")
        else:
            print("Task is completed")

    #called in view_tasks(), used to make object data readable
    def __str__(self):
        if self.dependencies == "":
            self.dependencies = "none"
        return f"Name: {self.name} | Due Date: {self.due_date} | Category: {self.category} | Priority: {self.priority} | Completed: {self.priority} | Dependencies: {self.dependencies}"