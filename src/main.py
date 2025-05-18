#Imports Task and TaskManager modules from classes
from classes.Task import *
from classes.TaskManager import *

#makes TaskManager functions callable 
task_manager = TaskManager()

#while loop for user to enter commands
while True:

    print(f"\nOptions:\n1: Add task\n2: View Tasks\n3: Mark Completed\n4: Sort\n5: Quit")
    user_input = input(">> ")
    
    #takes user input and calls function from TaskManager according to the command entered
    if user_input == "1":
        task_manager.add_tasks()
    elif user_input == "2":
        task_manager.view_tasks()
    elif user_input == "3":
        task_manager.mark_task_complete()
    elif user_input == "5":
        print("Exiting program")
        break
    elif user_input == "4":
        task_manager.sort()