from collections import deque

projects = [
    {"id": 1, "name": "Building A", "location": "Kigali", "status": "Planning", "description": "Construction of a multi-floor office building."},
    {"id": 2, "name": "Bridge B", "location": "Gisenyi", "status": "Foundation", "description": "Building a new bridge across the river."},
    {"id": 3, "name": "Warehouse C", "location": "Butare", "status": "Design", "description": "Warehouse construction for logistics."},
    {"id": 4, "name": "Park D", "location": "Musanze", "status": "Completion", "description": "Public park with recreational facilities."}
]

task_queue = deque()
undo_stack = []

ongoing_projects = []

def display_projects():
    print("\nOngoing Projects:")
    for project in projects:
        print(f"{project['id']}: {project['name']} | Location: {project['location']} | Status: {project['status']}")
        print(f"  Description: {project['description']}")
    print()

def schedule_task(task_description, project_id, task_time):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        task = {"project": project, "task_description": task_description, "task_time": task_time}
        task_queue.append(task)
        undo_stack.append({"action": "schedule", **task})
        print(f"Task '{task_description}' scheduled for {project['name']} at {task_time}!")
    else:
        print("Project not found!")

def undo_task():
    if undo_stack:
        last_action = undo_stack.pop()
        if last_action["action"] == "schedule":
            task_to_remove = {"project": last_action["project"], "task_description": last_action["task_description"], "task_time": last_action["task_time"]}
            if task_to_remove in task_queue:
                task_queue.remove(task_to_remove)
                print(f"Task '{last_action['task_description']}' for {last_action['project']['name']} has been undone.")
    else:
        print("No actions to undo.")

def view_ongoing_projects():
    print("\nOngoing Projects:")
    if ongoing_projects:
        for project in ongoing_projects:
            print(f"Project: {project['name']} - Location: {project['location']} - Status: {project['status']}")
    else:
        print("No ongoing projects currently.")

def update_project_status(project_id, new_status):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        previous_status = project['status']
        project['status'] = new_status
        undo_stack.append({"action": "update_status", "project": project, "previous_status": previous_status})
        print(f"Project '{project['name']}' status updated from '{previous_status}' to '{new_status}'.")
    else:
        print("Project not found.")

def main():
    while True:
        print("\nConstruction Project Manager")
        print("1. Display ongoing projects")
        print("2. Schedule a new task")
        print("3. Undo last task or project status change")
        print("4. Update project status")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_projects()
        elif choice == '2':
            project_id = int(input("Enter project ID to schedule task: "))
            task_description = input("Enter task description: ")
            task_time = input("Enter scheduled time for task (e.g., '2024-11-15 10:00'): ")
            schedule_task(task_description, project_id, task_time)
        elif choice == '3':
            undo_task()
        elif choice == '4':
            project_id = int(input("Enter project ID to update status: "))
            new_status = input("Enter new status for the project: ")
            update_project_status(project_id, new_status)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
