class Task:
    def __init__(self,name, due_date, category, priority, completed, dependencies):
        self.name = name 
        self.due_date = due_date
        self.category = category
        self.priority = priority
        self.completed = False
        self.dependencies = dependencies

    def status(self):
        if self.completed == False:
            print("Task is not completed")
        else:
            print("Task is completed")

