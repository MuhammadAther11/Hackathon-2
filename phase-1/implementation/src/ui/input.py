import curses

def handle_input(ui, key):
    if key == ord('q') or key == 27: # q or ESC
        if len(ui.screen_stack) > 1:
            ui.screen_stack.pop()
        else:
            ui.running = False
        return

    if ui.screen_stack:
        ui.screen_stack[-1].handle_key(key)
