# UI Theme and Constants
import curses

# Colors
COLOR_DEFAULT = 0
COLOR_HEADER = 1
COLOR_SUCCESS = 2
COLOR_ERROR = 3
COLOR_HIGHLIGHT = 4

def init_colors():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(COLOR_HEADER, curses.COLOR_CYAN, -1)
    curses.init_pair(COLOR_SUCCESS, curses.COLOR_GREEN, -1)
    curses.init_pair(COLOR_ERROR, curses.COLOR_RED, -1)
    curses.init_pair(COLOR_HIGHLIGHT, curses.COLOR_BLACK, curses.COLOR_WHITE)

# Menu items
MENU_ITEMS = [
    "1. Add Task",
    "2. List Tasks",
    "3. Show Task Details",
    "4. Update Task",
    "5. Complete Task",
    "6. Delete Task",
    "7. Set Priority",
    "8. Exit"
]
