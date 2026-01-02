# Phase 1: In-Memory Python Console Todo Application

This is the Phase 1 implementation of the AI-Native Todo Application. It is a strictly in-memory CLI tool built with the Python standard library.

## Features
- Add tasks with descriptions
- List all tasks with status and priority
- Show detailed task information
- Update task descriptions
- Mark tasks as complete
- Delete tasks
- Set task priority (Low, Medium, High)

## Prerequisites
- Python 3.10+

## How to Run

From the root of the repository:

```bash
cd phase-1/implementation
# To launch the interactive Terminal UI (Default)
python -m src

# To use the original CLI arguments mode
python -m src <command> [arguments]
```

### Available Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `add` | `python -m src add "Task description"` | Add a new task |
| `list` | `python -m src list` | List all tasks |
| `show` | `python -m src show <id>` | Show task details |
| `update` | `python -m src update <id> "New description"` | Update task text |
| `complete` | `python -m src complete <id>` | Mark task as complete |
| `delete` | `python -m src delete <id>` | Remove a task |
| `set-priority` | `python -m src set-priority <id> <low\|medium\|high>` | Set task priority |

## Limitations
- **No Persistence**: Data is lost when the command finishes. Since this is a CLI that executes and exits, in-memory storage only persists during a single command execution. *Note: In Phase 1, the requirement was in-memory, but since it's a CLI and not a long-running process, data doesn't persist between separate command runs.*
- **Single User**: No multi-user or authentication support.

## Spec-Driven Development
This implementation was generated entirely by AI agents based on the specifications found in `specs/001-phase-1-todo-cli/`.
