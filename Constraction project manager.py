from collections import deque

undo_stack = []
task_queue = deque()
ongoing_projects = []

def add_task(task):
    task_queue.append(task)
    print(f"Task added: {task}")

def complete_task():
    if task_queue:
        completed_task = task_queue.popleft()
        ongoing_projects.append(completed_task)
        print(f"Task completed: {completed_task}")
        undo_stack.append(completed_task)  
    else:
        print("No tasks to complete.")
        
def undo_last_change():
    if undo_stack:
        last_task = undo_stack.pop()
        ongoing_projects.remove(last_task)
        task_queue.appendleft(last_task)  
        print(f"Undo last change: {last_task}")
    else:
        print("No changes to undo.")

def display_projects():
    if not ongoing_projects:
        print("There is no ongoing project")
    else:
        print("Ongoing Projects:")
        for project in ongoing_projects:
            print(f"- {project}")


add_task("Build foundation")
add_task("Frame walls")
add_task("installation")
complete_task()
display_projects()
undo_last_change()
display_projects()
print(task_queue)