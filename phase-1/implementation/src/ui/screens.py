import curses
from src.ui.theme import MENU_ITEMS, COLOR_HEADER, COLOR_HIGHLIGHT
from src.services.todo_service import todo_manager

class BaseScreen:
    def __init__(self, ui):
        self.ui = ui

    def draw(self, stdscr):
        pass

    def handle_key(self, key):
        pass

class MainMenuScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)
        self.selected_index = 0

    def draw(self, stdscr):
        h, w = stdscr.getmaxyx()
        title = "AI-NATIVE TODO - MAIN MENU"
        stdscr.addstr(1, (w - len(title)) // 2, title, curses.color_pair(COLOR_HEADER) | curses.A_BOLD)

        for i, item in enumerate(MENU_ITEMS):
            x = (w - 20) // 2
            y = 4 + i
            if i == self.selected_index:
                stdscr.attron(curses.color_pair(COLOR_HIGHLIGHT))
                stdscr.addstr(y, x, item)
                stdscr.attroff(curses.color_pair(COLOR_HIGHLIGHT))
            else:
                stdscr.addstr(y, x, item)

        instructions = "Use Arrows to navigate, Enter to select, 'q' to exit"
        stdscr.addstr(15, (w - len(instructions)) // 2, instructions, curses.A_DIM)

    def handle_key(self, key):
        if key == curses.KEY_UP:
            self.selected_index = (self.selected_index - 1) % len(MENU_ITEMS)
        elif key == curses.KEY_DOWN:
            self.selected_index = (self.selected_index + 1) % len(MENU_ITEMS)
        elif key == 10: # Enter
            self.execute_selection()
        elif ord('1') <= key <= ord('8'):
            self.selected_index = int(chr(key)) - 1
            self.execute_selection()

    def execute_selection(self):
        if self.selected_index == 7: # Exit
            self.ui.running = False
            return

        if self.selected_index == 1: # List Tasks
            self.ui.screen_stack.append(TaskListScreen(self.ui))
        elif self.selected_index == 0: # Add Task
            self.ui.screen_stack.append(PromptScreen(self.ui, "Enter task description: ", self.add_task_callback))
        elif self.selected_index == 2: # Show Details
            self.ui.screen_stack.append(PromptScreen(self.ui, "Enter task ID: ", self.show_details_callback))
        elif self.selected_index == 3: # Update Task
             self.ui.screen_stack.append(PromptScreen(self.ui, "Enter task ID to update: ", self.update_id_callback))
        elif self.selected_index == 4: # Complete Task
             self.ui.screen_stack.append(PromptScreen(self.ui, "Enter task ID to complete: ", self.complete_callback))
        elif self.selected_index == 5: # Delete Task
             self.ui.screen_stack.append(PromptScreen(self.ui, "Enter task ID to delete: ", self.delete_callback))
        elif self.selected_index == 6: # Set Priority
             self.ui.screen_stack.append(PromptScreen(self.ui, "Enter task ID: ", self.priority_id_callback))

    def add_task_callback(self, text):
        try:
            todo_manager.add_task(text)
            self.ui.set_status("Success: Task added!")
        except Exception as e:
            self.ui.set_status(f"Error: {e}")

    def show_details_callback(self, text):
        try:
            task_id = int(text)
            task = todo_manager.get_task(task_id)
            if task:
                self.ui.screen_stack.append(TaskDetailScreen(self.ui, task))
            else:
                self.ui.set_status(f"Error: Task {task_id} not found")
        except ValueError:
            self.ui.set_status("Error: ID must be a number")

    def update_id_callback(self, text):
        try:
            task_id = int(text)
            task = todo_manager.get_task(task_id)
            if task:
                self.ui.screen_stack.append(PromptScreen(self.ui, f"New description for #{task_id}: ", lambda desc: self.update_desc_callback(task_id, desc)))
            else:
                self.ui.set_status(f"Error: Task {task_id} not found")
        except ValueError:
            self.ui.set_status("Error: ID must be a number")

    def update_desc_callback(self, task_id, desc):
        try:
            todo_manager.update_task(task_id, desc)
            self.ui.set_status(f"Success: Task {task_id} updated")
        except Exception as e:
            self.ui.set_status(f"Error: {e}")

    def complete_callback(self, text):
        try:
            task_id = int(text)
            todo_manager.complete_task(task_id)
            self.ui.set_status(f"Success: Task {task_id} completed")
        except Exception as e:
            self.ui.set_status(f"Error: {e}")

    def delete_callback(self, text):
        try:
            task_id = int(text)
            todo_manager.delete_task(task_id)
            self.ui.set_status(f"Success: Task {task_id} deleted")
        except Exception as e:
            self.ui.set_status(f"Error: {e}")

    def priority_id_callback(self, text):
        try:
            task_id = int(text)
            task = todo_manager.get_task(task_id)
            if task:
                self.ui.screen_stack.append(PromptScreen(self.ui, "Enter priority (low/medium/high): ", lambda p: self.priority_val_callback(task_id, p)))
            else:
                self.ui.set_status(f"Error: Task {task_id} not found")
        except ValueError:
            self.ui.set_status("Error: ID must be a number")

    def priority_val_callback(self, task_id, priority):
        try:
            todo_manager.set_priority(task_id, priority)
            self.ui.set_status(f"Success: Priority set to {priority}")
        except Exception as e:
            self.ui.set_status(f"Error: {e}")

class TaskListScreen(BaseScreen):
    def draw(self, stdscr):
        h, w = stdscr.getmaxyx()
        title = "TASK LIST"
        stdscr.addstr(1, (w - len(title)) // 2, title, curses.color_pair(COLOR_HEADER) | curses.A_BOLD)

        tasks = todo_manager.get_all_tasks()
        if not tasks:
            stdscr.addstr(4, (w - 15) // 2, "No tasks found.")
        else:
            header = f"{'ID':3} | {'Status':6} | {'Priority':7} | {'Description'}"
            stdscr.addstr(3, 2, header, curses.A_UNDERLINE)
            for i, task in enumerate(tasks):
                status = "[X]" if task.is_completed else "[ ]"
                row = f"{task.id:3} | {status:6} | {task.priority.upper():7} | {task.description}"
                if h > 4 + i:
                    stdscr.addstr(4 + i, 2, row[:w-3])

        instr = "Press 'q' or ESC to return to menu"
        stdscr.addstr(h-2, (w - len(instr)) // 2, instr, curses.A_DIM)

class TaskDetailScreen(BaseScreen):
    def __init__(self, ui, task):
        super().__init__(ui)
        self.task = task

    def draw(self, stdscr):
        h, w = stdscr.getmaxyx()
        stdscr.addstr(2, 2, f"TASK DETAILS (ID: {self.task.id})", curses.color_pair(COLOR_HEADER) | curses.A_BOLD)
        stdscr.addstr(4, 4, f"Description: {self.task.description}")
        stdscr.addstr(5, 4, f"Status:      {'Completed' if self.task.is_completed else 'Pending'}")
        stdscr.addstr(6, 4, f"Priority:    {self.task.priority.upper()}")

        instr = "Press any key to return"
        stdscr.addstr(h-2, (w - len(instr)) // 2, instr, curses.A_DIM)

    def handle_key(self, key):
        self.ui.screen_stack.pop()

class PromptScreen(BaseScreen):
    def __init__(self, ui, prompt_text, callback):
        super().__init__(ui)
        self.prompt_text = prompt_text
        self.callback = callback
        self.input_text = ""

    def draw(self, stdscr):
        h, w = stdscr.getmaxyx()
        curses.curs_set(1) # Show cursor
        stdscr.addstr(h // 2 - 1, (w - len(self.prompt_text)) // 2, self.prompt_text)
        stdscr.addstr(h // 2, (w - 20) // 2, self.input_text + "_")

    def handle_key(self, key):
        if key == 10: # Enter
            curses.curs_set(0)
            self.ui.screen_stack.pop()
            self.callback(self.input_text)
        elif key == curses.KEY_BACKSPACE or key == 127 or key == 8:
            self.input_text = self.input_text[:-1]
        elif 32 <= key <= 126:
            self.input_text += chr(key)
