from classes.Task import *

class TaskManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating singleton intance")
            cls._instance = super(TaskManager, cls).__new__(cls)
        else:
            print("Loading an existing instance")
        return cls._instance
    
    def __init__(self, tasks=[], observers=[]):
        self.tasks = tasks
        self.observers = observers

    def add_tasks():
        pass

