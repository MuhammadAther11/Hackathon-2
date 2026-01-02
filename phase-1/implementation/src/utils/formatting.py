def format_success(message):
    print(f"Success: {message}")

def format_error(message):
    print(f"Error: {message}")

def format_task(task):
    status = "[X]" if task.is_completed else "[ ]"
    return f"{task.id:3} | {status} | {task.priority.upper():7} | {task.description}"

def format_task_list(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print(f"{'ID':3} | {'Status':3} | {'Priority':7} | {'Description'}")
    print("-" * 60)
    for task in tasks:
        print(format_task(task))
