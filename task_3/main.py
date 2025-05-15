from colorama import Fore
import sys
from pathlib import Path

def main():
    if len(sys.argv) >= 2:
        path = Path(sys.argv[1])
        if path.exists() and path.is_dir():
            process_file_and_dir(path)

        else:
            print(f"{Fore.RED} Path not exists or path is not directory {Fore.RESET}")
            sys.exit(-1)
    else:
        print(f"{Fore.RED} Program requires 1 argument (path) {Fore.RESET}")
        sys.exit(-1)

def process_file_and_dir(path: Path, depth=0):
    for object in path.iterdir():
        if object.is_dir():
            print(f"{Fore.BLUE} {' ' * depth}{object.name}/ {Fore.RESET}")

            process_file_and_dir(object, depth + 1)
        else:
            print(f"{Fore.GREEN} {' ' * depth}{object.name} {Fore.RESET}")


if __name__ == "__main__":
    main()
