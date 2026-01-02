from src.models.task import TodoTask

class TodoManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, description):
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        task = TodoTask(id=self._next_id, description=description.strip())
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, description):
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Invalid task ID: {task_id}")

        task.description = description.strip()
        return task

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Invalid task ID: {task_id}")

        task.is_completed = True
        return task

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Invalid task ID: {task_id}")

        self.tasks.remove(task)
        return True

    def set_priority(self, task_id, priority):
        allowed_priorities = ["low", "medium", "high"]
        if priority.lower() not in allowed_priorities:
            raise ValueError(f"Invalid priority level: {priority}. Must be one of {allowed_priorities}")

        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Invalid task ID: {task_id}")

        task.priority = priority.lower()
        return task

# Singleton instance for in-memory storage during runtime
todo_manager = TodoManager()
