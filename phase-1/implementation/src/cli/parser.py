import argparse

def get_parser():
    parser = argparse.ArgumentParser(prog="python -m src", description="Phase 1 In-Memory Todo CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # List
    subparsers.add_parser("list", help="List all tasks")

    # Show
    show_parser = subparsers.add_parser("show", help="Show task details")
    show_parser.add_argument("id", type=int, help="Task ID")

    # Update
    update_parser = subparsers.add_parser("update", help="Update task description")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", help="New description")

    # Complete
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # Set-priority
    priority_parser = subparsers.add_parser("set-priority", help="Set task priority")
    priority_parser.add_argument("id", type=int, help="Task ID")
    priority_parser.add_argument("level", choices=["low", "medium", "high"], help="Priority level")

    return parser
