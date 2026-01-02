import sys
from src.cli.parser import get_parser
from src.cli.handlers import handle_command
from src.ui.loop import start_ui

def main():
    # If no arguments provided, launch the interactive UI
    if len(sys.argv) == 1:
        start_ui()
        return

    parser = get_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    try:
        handle_command(args)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
