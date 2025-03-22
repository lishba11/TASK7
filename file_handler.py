import os

def read_tasks(file_path):
    """Read tasks from a file. Create the file if it doesn't exist."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def write_tasks(file_path, tasks):
    """Write tasks to a file."""
    try:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except Exception as e:
        print(f"Error writing to file: {e}")
