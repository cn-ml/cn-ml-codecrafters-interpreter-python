import sys
from loxscanner import LoxScanner


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    scanner = LoxScanner(file_contents)
    for token in scanner.scan_tokens():
        print(token)


if __name__ == "__main__":
    main()
