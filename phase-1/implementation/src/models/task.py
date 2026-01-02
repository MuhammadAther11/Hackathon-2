from dataclasses import dataclass

@dataclass
class TodoTask:
    id: int
    description: str
    is_completed: bool = False
    priority: str = "medium"
