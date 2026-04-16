tasks = []

def add_task(task:str):
    tasks.append(task)

def show_tasks():
    return tasks

def delete_task(index:int):
    tasks.pop(index)