def add_task(tasks, task):
    """Add a task to the list."""
    tasks.append(task)
    return tasks

def remove_task(tasks, task_number):
    """Remove a task by its number."""
    try:
        task_index = task_number - 1
        if task_index < 0 or task_index >= len(tasks):
            raise IndexError("Task number out of range.")
        tasks.pop(task_index)
        return tasks
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        return tasks

def update_task(tasks, task_number, new_task):
    """Update a task by its number."""
    try:
        task_index = task_number - 1
        if task_index < 0 or task_index >= len(tasks):
            raise IndexError("Task number out of range.")
        tasks[task_index] = new_task
        return tasks
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        return tasks

def view_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
