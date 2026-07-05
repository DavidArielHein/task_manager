import sys
import json

class Task:
    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

with open('data.json', 'w', encoding='utf-8') as json_file:
    if sys.argv[1] == 'add' and sys.argv[2]:
        pass