"""
from Ali Alarkawazi and Abdel-Hamid Attia

Task at 04.07.2024
Building a Simple To-Do List without reduce
Objective:
To develop a simple command-line To-Do List application without (map, filter, reduce). 
This project will help you understand how to use these Python features in practical scenarios.
Instructions:
    1. Project Overview:
        ○ Create a command-line application that allows users to add, remove, view tasks, view task lengths, filter tasks by length, and calculate the total length of all tasks.
    2. Requirements:
        ○ List Comprehension: Use list comprehensions where applicable.
        ○ Dict Comprehension: Use dictionary comprehensions to store tasks.
        ○ Functional Programming: Use map, filter, and reduce for task processing.
    3. Steps to Complete the Project:
        Step 1: Initialize the Project
        ○ Create a Python file named todo_list.py.
        ○ Define a class ToDoList to encapsulate all functionalities.
    4. Step 2: Define the ToDoList Class
        ○ Define the __init__ method to initialize an empty dictionary to store tasks.
    5. Step 3: Implement Add and Remove Task Functions
        ○ add_task(self, task): Add a task to the dictionary with a unique ID.
        ○ remove_task(self, task_id): Remove a task from the dictionary using the task ID.
    6. Step 4: Implement View Tasks Function
        ○ view_tasks(self): Print all tasks with their IDs.
    7. Step 5: Implement Functional Programming Methods
        ○ get_task_lengths(self): Use map to create a list of task lengths.
        ○ get_long_tasks(self, min_length): Use filter to get tasks longer than min_length.
        ○ get_total_task_length(self): Use reduce to calculate the total length of all tasks.
    8. Step 6: Implement the Main Program Loop
        ○ Create a main loop to display a menu and call appropriate methods based on user input.
"""
# Define the ToDoList Class
class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.id = 1

# add_task(self, task): Add a task to the dictionary with a unique ID.
    def add_task(self, task):
        self.tasks[self.id] = task
        self.id += 1

# remove_task(self, task_id): Remove a task from the dictionary using the task ID.
    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            print(f"Task ID {task_id} out of range.")

# view_tasks(self): Print all tasks with their IDs.
    def view_tasks(self):
        for task_id, task in self.tasks.items():
            print(f"{task_id}: {task}")

# get_task_lengths(self): Use map to create a list of task lengths.
    def get_task_lengths(self):
        return [len(task) for task in self.tasks.values()]

#get_long_tasks(self, min_length): Use filter to get tasks longer than min_length.
    def get_long_tasks(self, min_length):
        return {task_id: task for task_id, task in self.tasks.items() if len(task) >= min_length}

#get_total_task_length(self): Use reduce to calculate the total length of all tasks.
    def get_total_task_length(self):
        return sum(len(task) for task in self.tasks.values())



#Create a main loop to display a menu and call appropriate methods based on user input.

def main():
    todo_list = ToDoList()

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. View Task Lengths")
        print("5. Filter Tasks by Length")
        print("6. Get Total Task Length")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter new task: ")
            todo_list.add_task(task)
        elif choice == 2:
            task_id = int(input("Enter task_id to remove = "))
            todo_list.remove_task(task_id)
        elif choice == 3:
            todo_list.view_tasks()
        elif choice == 4:
            lengths = todo_list.get_task_lengths()
            print("Task Lengths = ", lengths)
        elif choice == 5:
            min_length = 5
            min_length = int(input("Enter the minimum task length to filter = "))
            long_tasks = todo_list.get_long_tasks(min_length)
            print("long Tasks = ", long_tasks)
        elif choice == 6:
            total_length = todo_list.get_total_task_length()
            print("Total Task Length = ", total_length)
        elif choice == 7:
            break
        else:
            print("try again.")

if __name__ == "__main__":
    main()
