# Modules to manage inputs of the user, json files and current times
import sys
import json
from datetime import datetime

class Task:
    # Default task
    def __init__(self):
        self.__id = 0
        self.__description = 'No description'
        self.__status = 'No status'
        self.__created_at = 'No date'
        self.__updated_at = 'No date'
    

    def create_task(self, id, description, status, created_at, updated_at):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__created_at = created_at
        self.__updated_at = updated_at

    # Formatting the data to match the json format
    def format_json(self):
        return {
            'id':self.__id,
            'description':self.__description,
            'status':self.__status,
            'created_at':self.__created_at,
            'updated_at':self.__updated_at
        }

# Constants for checking commands from the user
VALID_COMMANDS = ['add', 'update', 'delete', 'change-status', 'list', 'commands-list']
VALID_STATUS = ['todo', 'in-progress', 'done']

COMMAND_HELP = '''
-------------------- Command list --------------------
Add new task: add <task description>
Update existing task: update <task id> <new description>
Delete task: delete <task id>
Change status of a task: change-status <task id> <new status [todo, in-progress, done]>
'''


def main():
    # Verifying if prompted enough arguments and correct commands
    if len(sys.argv) < 2:
        print('Error: No command provided.\nTry "commands-list" to see the available commands')
        return
    elif sys.argv[1] not in VALID_COMMANDS:
        print(f'Error: "{sys.argv[1]}" not recognized.\nTry "commands-list" to see the available commands')
        return

    # Retrieving the user's command
    command = sys.argv[1]
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Checking what action the user wants to do
    if command == 'add':
        # Checking if there are task name
        if len(sys.argv) < 3:
            print('Error: Missing task description.')

        # Getting the actual data of the file and creating a new task object
        tasks_list = get_file_data()
        new_task = Task()

        # Adding the new task to the list
        if not tasks_list:  
            new_task.create_task(1, sys.argv[2], 'todo', current_time, current_time)
            print(f'Task "{sys.argv[2]}" created successfully (ID: 1)')
        else:
            new_task.create_task(tasks_list[-1]['id'] + 1, sys.argv[2], 'To do', current_time, current_time)
            print(f'Task "{sys.argv[2]}" created successfully (ID: {tasks_list[-1]['id'] + 1})')
        
        # Updating the json file
        tasks_list.append(new_task.format_json())
        update_file(tasks_list)
    
    elif command == 'update':
        tasks_list = get_file_data()
        
        if len(sys.argv) < 3:
            print('Error: Missing task ID')
            return
        elif len(sys.argv) < 4:
            print('Error: Missing new description')
            return
        
        id = int(sys.argv[2])
        new_desc = sys.argv[3]
        
        # Updating the description of the task
        for task in tasks_list:
            if task['id'] == id:
                print(f'Task "{task['description']}" updated successfully to "{new_desc}"')
                task['description'] = new_desc
                task['updated_at'] = current_time
                break
        else:
            print('Task not found')
        
        # Updating the json file
        update_file(tasks_list)
    
    elif command == 'delete':
        tasks_list = get_file_data()
        
        if len(sys.argv) < 3:
            print('Error: Missing task ID')
            return
        
        id = int(sys.argv[2])
        
        # Removing the task from the list
        for i, task in enumerate(tasks_list):
            if task['id'] == id:
                print(f'Task "{task['description']}" deleted successfully')
                tasks_list.remove(task)
                break
        else:
            print('Task not found')
        
        # Updating the json file
        update_file(tasks_list)
    
    elif command == 'change-status':
        tasks_list = get_file_data()
        
        if len(sys.argv) < 3:
            print('Error: Missing task ID')
            return
        elif len(sys.argv) < 4:
            print('Error: Missing status')
            return
        
        id = int(sys.argv[2])
        if sys.argv[3] not in VALID_STATUS:
            print('Status not recognized')
            return
        
        for task in tasks_list:
            if task['id'] == id:
                task['status'] = sys.argv[3]
                task['updated_at'] = current_time
                print(f'"{task['description']}" marked as "{sys.argv[3]}"')
                break
        else:
            print('Task not found')
        
        # Updating the json file
        update_file(tasks_list)
    
    elif command == 'list':
        tasks_list = get_file_data()
    
        
        if len(sys.argv) < 3:
            for task in tasks_list:
                print(
                    f"Task: {task['description']}\n"
                    f"Id: {task['id']}\n"
                    f"Status: {task['status']}\n"
                    f"Created at: {task['created_at']}\n"
                    f"Updated: {task['updated_at']}\n"
                )
        elif sys.argv[2] == 'todo':
            for task in tasks_list:
                if task['status'] == 'todo':
                    print(
                        f"Task: {task['description']}\n"
                        f"Id: {task['id']}\n"
                        f"Status: {task['status']}\n"
                        f"Created at: {task['created_at']}\n"
                        f"Updated: {task['updated_at']}\n"
                    )
        elif sys.argv[2] == 'in-progress':
            for task in tasks_list:
                if task['status'] == 'in-progress':
                    print(
                        f"Task: {task['description']}\n"
                        f"Id: {task['id']}\n"
                        f"Status: {task['status']}\n"
                        f"Created at: {task['created_at']}\n"
                        f"Updated: {task['updated_at']}\n"
                    )
        elif sys.argv[2] == 'done':
            for task in tasks_list:
                if task['status'] == 'done':
                    print(
                        f"Task: {task['description']}\n"
                        f"Id: {task['id']}\n"
                        f"Status: {task['status']}\n"
                        f"Created at: {task['created_at']}\n"
                        f"Updated: {task['updated_at']}\n"
                    )
        else:
            print('Filter not recognized')
    
    elif command == 'commands-list':
        print(COMMAND_HELP)

# Function for getting the data of the file, or creating a new if not exists
def get_file_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump([], json_file)
        return []
    except json.JSONDecodeError:
        return []

# Function for updating the file with new data
def update_file(new_tasks):
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(new_tasks, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()