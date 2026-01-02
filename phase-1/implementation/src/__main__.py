import sys
from src.cli.parser import get_parser
from src.cli.handlers import handle_command

def main():
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
