import sys
from typing import Sequence
from .lexing.error import ParseException
from .lox import Scanner, Token, Parser


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    match command:
        case "tokenize":
            tokenize(filename, output=True)
        case "parse":
            tokens = tokenize(filename)
            match parse(tokens):
                case [single]:
                    print(single)
                case other:
                    raise Exception(f"Parsed {len(other)} objects!")

        case other:
            print(f"Unknown command: {other}", file=sys.stderr)
            exit(1)


def parse(tokens: Sequence[Token]):
    parser = Parser(tokens)
    try:
        return list(parser.execute())
    except ParseException:
        exit(65)


def tokenize(filename: str, output: bool = False) -> list[Token]:
    with open(filename) as file:
        file_contents = file.read()

    scanner = Scanner(file_contents)
    tokens = list(scanner.execute())
    if output:
        for token in tokens:
            print(token)
    if scanner.errors is not None:
        exit(65)
    return tokens


if __name__ == "__main__":
    main()
