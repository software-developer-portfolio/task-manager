# Task Manager - A command-line task manager written in Python

# Imports
import os
import pickle
from datetime import datetime

# Initialize an empty list to store tasks
tasks = []
# Define the file name for storing tasks
TASK_MANAGER_FILE = "tasks.pkl"
# Define a class to represent each task
class Task():
    def __init__(self, title, created_at, is_completed=False):
        self.title = title
        self.created_at = created_at
        self.is_completed = is_completed

# Function to save tasks to the pickle file
def save_tasks():
    with open(TASK_MANAGER_FILE, "wb") as file:
        pickle.dump(tasks, file)

# Function to load tasks from the pickle file
def load_tasks():
    global tasks
    if os.path.exists(TASK_MANAGER_FILE):
        with open(TASK_MANAGER_FILE, "rb") as file:
            tasks = pickle.load(file)

# Function to add a new task
def add_task():
    # Prompt the user to enter a task
    title = input("Enter a task: ")
    # Format the date and time
    created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # Create the task
    task = Task(title, created_at)
    # Append each task to the tasks list
    tasks.append(task)
    # Save the tasks to the pickle file
    save_tasks()

# Function to print all tasks
def print_tasks():
    print("+----+-----------------------------------------------+---------------------+----------------+")
    print("| ID |                     Task                      |     Created At      |    Completed   |")
    print("+----+-----------------------------------------------+---------------------+----------------+")

    # Iterate through the tasks list and print each task
    for index, task in enumerate(tasks):
        print(f"| {index + 1:2} | {task.title:45} | {task.created_at:19} | {"✅" if task.is_completed else "❌":^14}|")
    print("+----+-----------------------------------------------+---------------------+----------------+")

# Function to mark a task as completed
def mark_as_complete():
    # Call the print_tasks function to display the list of tasks
    print_tasks()
    try:
        # Prompt the user to enter the ID of the task they want to mark as completed
        task_id = int(input("Enter the ID of the task: ")) -1
        # Mark the task as completed
        tasks[task_id].is_completed = True
        # Save the tasks to the pickle file
        save_tasks()
    except IndexError:
        print("Invalid task ID. Please enter a valid ID.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

# Function to delete a task
def delete_task():
    # Call the print_tasks function to display the list of tasks
    print_tasks()
    try:
        # Prompt the user to enter the ID of the task they want to delete
        task_id = int(input("Enter the ID of the task: ")) -1
        # Delete the task
        del tasks[task_id]
        # Save the tasks to the pickle file
        save_tasks()
    except IndexError:
        print("Invalid task ID. Please enter a valid ID.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

# Function to display the options
def display_options():
    while True:
        print("Welcome to the Task Manager!")
        user_choice = input(" Type 'A' to add a task, 'D' to delete a task, 'C' to mark a task as complete, or 'Q' to quit").upper()
        if user_choice == "A":
            add_task()
        elif user_choice == "D":
            delete_task()
        elif user_choice == "C":
            mark_as_complete()
        elif user_choice == "Q":
            print("Thank you for using the Task Manager!")
            break
        else:
            print("Invalid option. Please enter a valid option.")
        print_tasks()

# Function to check if this is the first time the program is being run
def is_first_time():
    if os.path.exists(TASK_MANAGER_FILE):
        load_tasks()
        print_tasks()
    else:
        print("Welcome to the Task Manager!")
        add_task()
        print_tasks()

if __name__ == "__main__":
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")
    # Set the text to green and bold
    print("\033[32;1m]")
    is_first_time()
    display_options()
