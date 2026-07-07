# Task Tracker CLI

A lightweight and efficient Command Line Interface (CLI) application to track and manage your daily tasks. This project helps you organize your workflow by categorized task tracking (todo, in-progress, and done) with data persistence in a local JSON file.

Project link: https://roadmap.sh/projects/task-tracker

---

## Features

- **Add Tasks**: Quickly create new tasks with an auto-incrementing unique ID.
- **Update Tasks**: Modify descriptions of existing tasks easily.
- **Delete Tasks**: Remove outdated or completed tasks.
- **Status Management**: Mark tasks dynamically as `todo`, `in-progress`, or `done`.
- **Flexible Listing**: 
  - List all recorded tasks.
  - Filter tasks by completed status (`done`).
  - Filter tasks by uncompleted status (`todo`).
  - Filter tasks currently being worked on (`in-progress`).
- **Data Persistence**: All tasks are automatically saved and maintained in a standard `data.json` file.

---

## How To Use

The application runs directly from your command line. Execute commands by passing specific arguments. 

### 1. Adding a New Task
Create a new task by providing a description wrapped in quotes.
```bash
python task_manager add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### 2. Updating a Task Description

Modify an existing task's description using its unique ID.
```bash
python task_manager update 1 "Buy groceries and cook dinner"
# Output: Task 1 updated successfully
```

### 3. Deleting a Task

Permanently remove a task using its ID.
```bash
python task_manager delete 1
# Output: Task 1 deleted successfully
```

### 4. Updating Task Status

Change the progress status of your tasks dynamically.

#### Mark as In-Progress:

```bash
python task_manager change-status 1 in-progress
# Output: Task 1 marked as in-progress
```

#### Mark as In-Progress:

```bash
python task_manager change-status 1 done
# Output: Task 1 marked as in-progress
```

### 5. Listing Tasks

View your tasks based on global list or specific statuses.

#### List All Tasks:
```bash
python task_manager list
```

#### List Done Tasks:
```bash
python task_manager list done
```

#### List To Do Tasks:
```bash
python task_manager list todo
```

#### List In progress Tasks:
```bash
python task_manager list in-progress
```