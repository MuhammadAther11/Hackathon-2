import curses
import time
from src.ui.theme import init_colors
from src.ui.input import handle_input

class UILoop:
    def __init__(self):
        self.running = True
        self.screen_stack = []
        self.status_message = ""
        self.status_expiry = 0

    def set_status(self, message, duration=2):
        self.status_message = message
        self.status_expiry = time.time() + duration

    def run(self, stdscr):
        # Initial curses setup
        curses.curs_set(0) # Hide cursor
        init_colors()

        # Start with main menu if stack is empty
        from src.ui.screens import MainMenuScreen
        if not self.screen_stack:
            self.screen_stack.append(MainMenuScreen(self))

        while self.running:
            stdscr.erase()

            # Clear expired status messages
            if time.time() > self.status_expiry:
                self.status_message = ""

            # Draw current screen
            if self.screen_stack:
                current_screen = self.screen_stack[-1]
                current_screen.draw(stdscr)

            # Draw status message if exists
            if self.status_message:
                h, w = stdscr.getmaxyx()
                stdscr.addstr(h-1, 0, self.status_message, curses.color_pair(2) if "Success" in self.status_message else curses.color_pair(3))

            stdscr.refresh()

            # Handle input
            key = stdscr.getch()
            handle_input(self, key)

def start_ui():
    ui = UILoop()
    try:
        curses.wrapper(ui.run)
    except KeyboardInterrupt:
        pass
