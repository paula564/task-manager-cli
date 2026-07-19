import json
import time
import os
from pathlib import Path
from dataclasses import dataclass, asdict
from enum import Enum


#add a new task to the json file

class Status(Enum):
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3

@dataclass
class Task:
    description: str
    status: Enum



#to be added later: status, date created, last updated date



running = True
valid_commands = ["add", "update", "delete"]

#load all tasks
def load(file):
    path = Path(file)
    tasks = {}

    #if the path exists, read the file 
    if path.exists():
        file_size = os.path.getsize(path)
        if file_size > 0:
            with open(path, "r", encoding="utf-8") as file:
                tasks = json.load(file)
            return tasks 
        else:
            return None
    else:
        return None



def append(path, data):

    #erase the file to add the updated dictionary
    open(path, 'w').close()

    #append new dictionary
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def add(c, t):

    path = Path("data/tasks.json")
    tasks = {}
    file_size = os.path.getsize(path)

    #if the path exists, read the file, find the next item number
    #add the task to the data dictionary 
    if path.exists() and file_size > 0:
        with open(path, "r", encoding="utf-8") as file:
            tasks = json.load(file)

        index = len(tasks) + 1

        tasks[index] = asdict(Task(task, Status.TODO.name))
    else:
        #else, initialize to 1
        tasks[1] = asdict(Task(task, Status.TODO.name))

    append(path, tasks)


    

    
print("Welcome to Task Manager! Please select a valid command.\n")

while running:
    string = input()

    if string == "exit":
        print("Saving...")
        time.sleep(3)
        print("Tasks saved. See you soon!")
        break
    else:
        words_num = len(string.split())

        if words_num > 1:
            command, task = a, b = string.split(maxsplit=1)
        else:
            command = string

        if command == "add":
            add(command, task)
            print("Task added sucessfully")
        elif command == "list":
        
            if load("data/tasks.json") is not None:

                for id, task in load("data/tasks.json").items():
                    print(f"{id}. {task.get("description")}, Status: {task.get("status")}", end=" ")
                    print()
            else:
                print("whoops! no tasks yet. add one!")
                
        
                

        



        

      