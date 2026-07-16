import json
from pathlib import Path

#add a new task to the json file

running = True
valid_commands = ["add", "update", "delete"]



def append(path, data):

    #erase the file to add the updated dictionary
    open(path, 'w').close()

    #append new dictionary
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def add(c, t):

    path = Path("data/tasks.json")
    tasks = {}

    #if the path exists, read the file, find the next item number
    #add the task to the data dictionary 
    if path.exists():
        with open(path, "r", encoding="utf-8") as file:
            tasks = json.load(file)

        index = len(tasks) + 1
        tasks[index] = task
    else:
        #else, initialize to 1
        tasks[1] = task

    append(path, tasks)

    

while running:
    string = input()

    if string == "exit":
        print("see ya!")
        break
    else:
        command, task = a, b = string.split(maxsplit=1)

        if (command not in valid_commands):
            print("whoops! select a valid command (add, update, delete)")
        else:
            print(f"Command: {command} Task: {task}")


        if command == "add":
            add(command, task)
                

        



        

      