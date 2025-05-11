class Interface:
    def __init__(self,author,version,name,due_date,priority,category,complete,incomplete):
        self.author = author
        self.version = "0.0.0"
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.complete = False
        self.incomplete = True

