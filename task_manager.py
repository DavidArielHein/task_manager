import sys
import json
from datetime import datetime

class Task:
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
    
    
    def update_task(self, new_description, new_updated_at):
        self.__description = new_description
        self.__updated_at = new_updated_at
    
    
    def change_status(self, new_status):
        self.__status = new_status

    
    def format_json(self):
        return {
            'id':self.__id,
            'description':self.__description,
            'status':self.__status,
            'created_at':self.__created_at,
            'updated_at':self.__updated_at
        }

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
    if len(sys.argv) < 2:
        print('Error: No command provided.\nTry "commands-list" to see the available commands')
        return
    elif sys.argv[1] not in VALID_COMMANDS:
        print(f'Error: "{sys.argv[1]}" not recognized.\nTry "commands-list" to see the available commands')
        return

    command = sys.argv[1]
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if command == 'add':
        if len(sys.argv) < 3:
            print('Error: Missing task description.')

        tasks_list = get_file_data()
        new_task = Task()

        if not tasks_list:  
            new_task.create_task(1, sys.argv[2], 'To do', current_time, current_time)
        else:
            new_task.create_task(tasks_list[-1]['id'] + 1, sys.argv[2], 'To do', current_time, current_time)
            
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
        
        for task in tasks_list:
            if task['id'] == id:
                task['description'] = new_desc
                task['updated_at'] = current_time
                break
        else:
            print('Task not found')
        
        update_file(tasks_list)
    
    elif command == 'delete':
        tasks_list = get_file_data()
        
        if len(sys.argv) < 3:
            print('Error: Missing task ID')
            return
        
        id = int(sys.argv[2])
        
        for i, task in enumerate(tasks_list):
            if task['id'] == id:
                tasks_list.remove(task)
                break
        else:
            print('Task not found')
        
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
        new_status = sys.argv[3]
        if new_status not in VALID_STATUS:
            print('Status not recognized')
            return
        
        for task in tasks_list:
            if task['id'] == id:
                task['status'] = new_status
                task['updated_at'] = current_time
                break
        else:
            print('Task not found')
        
        update_file(tasks_list)
    
    elif command == 'list':
        tasks_list = get_file_data()
        for task in tasks_list:
            print(
                f"Task: {task['description']}\n"
                f"Id: {task['id']}\n"
                f"Status: {task['status']}\n"
                f"Created at: {task['created_at']}\n"
                f"Updated: {task['updated_at']}\n"
            )
    
    elif command == 'commands-list':
        print(COMMAND_HELP)

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


def update_file(new_tasks):
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(new_tasks, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()