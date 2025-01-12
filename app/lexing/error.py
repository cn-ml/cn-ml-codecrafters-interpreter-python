class ScanError(Exception):
    def __init__(
        self, source: str, line: int, position: int, lexeme: str, message: str
    ) -> None:
        self.source = source
        self.line = line
        self.position = position
        self.lexeme = lexeme
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"At line {self.line} position {self.position} {self.lexeme!r}: {self.message}"


class ParseException(Exception):
    pass
