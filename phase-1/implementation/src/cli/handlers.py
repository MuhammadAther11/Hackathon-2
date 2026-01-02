from src.services.todo_service import todo_manager
from src.utils.formatting import format_success, format_task_list, format_task

def handle_command(args):
    command = args.command

    if command == "add":
        task = todo_manager.add_task(args.description)
        format_success(f"Task added successfully with ID {task.id}")

    elif command == "list":
        tasks = todo_manager.get_all_tasks()
        format_task_list(tasks)

    elif command == "delete":
        todo_manager.delete_task(args.id)
        format_success(f"Task {args.id} deleted successfully")

    elif command == "show":
        task = todo_manager.get_task(args.id)
        if task:
            print(f"ID: {task.id}")
            print(f"Description: {task.description}")
            print(f"Status: {'Completed' if task.is_completed else 'Pending'}")
            print(f"Priority: {task.priority.capitalize()}")
        else:
            print(f"Error: Invalid task ID: {args.id}")

    elif command == "update":
        todo_manager.update_task(args.id, args.description)
        format_success(f"Task {args.id} updated successfully")

    elif command == "complete":
        todo_manager.complete_task(args.id)
        format_success(f"Task {args.id} marked as complete")

    elif command == "set-priority":
        todo_manager.set_priority(args.id, args.level)
        format_success(f"Priority for task {args.id} set to {args.level}")
