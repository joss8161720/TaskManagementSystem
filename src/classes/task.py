class Task:
    def __init__(self,name, due_date, user, category, priority, completed):
        self.name = name 
        self.due_date = due_date
        self.user = user
        self.category = category
        self.priority = priority
        self.completed = False

    def status(self):
        if self.completed == False:
            print("Task is not completed")
        else:
            print("Task is completed")