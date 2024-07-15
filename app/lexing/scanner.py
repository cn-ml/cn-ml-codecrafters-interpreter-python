from abc import ABC, abstractmethod
from sys import stderr
from typing import Callable
from .error import ScanError
from .tokens import Token


class Scanner[TToken, TLiteral](ABC):
    def __init__(self, source: str) -> None:
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.position = -1
        self.errors = None

    def scan_tokens(self):
        self.start = self.current
        while not self.exhausted():
            try:
                if (token := self.scan_token()) is not None:
                    yield token
            except ScanError as e:
                print(f"[line {e.line}] Error: {e.message}", file=stderr)
                self.errors = self.errors or list[ScanError]()
                self.errors.append(e)
            self.start = self.current
        yield self._make_eof()

    def _lexeme(self):
        return self.source[self.start : self.current]

    def _make(self, type: TToken, parse: Callable[[str], TLiteral] | None = None):
        lexeme = self._lexeme()
        literal = None if parse is None else parse(lexeme)
        return Token(type, lexeme, literal, self.line, self.position)

    def _peek(self):
        if self.exhausted():
            return "\0"
        return self.source[self.current]

    def _peek_ahead(self, amount: int):
        if self.current + amount >= len(self.source):
            return "\0"
        return self.source[self.current + amount]

    def _reset_line(self):
        self.line = self.line + 1
        self.position = 0

    def _advance(self):
        self.current = (current := self.current) + 1
        self.position = self.position + 1
        return self.source[current]

    def match(self, expected: str):
        if self.exhausted():
            return False
        if self.source[self.current] != expected:
            return False
        self.current = self.current + 1
        return True

    def _scan_error(self, message: str):
        return ScanError(self.source, self.line, self.position, self._lexeme(), message)

    def exhausted(self):
        return self.current >= len(self.source)

    @abstractmethod
    def scan_token(self) -> Token[TToken, TLiteral] | None: ...

    @abstractmethod
    def _make_eof(self) -> Token[TToken, TLiteral]: ...
