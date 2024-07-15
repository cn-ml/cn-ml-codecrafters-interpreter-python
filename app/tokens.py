from typing import TypeVar


T = TypeVar("T")


class Token[TToken, TLiteral]:
    def __init__(
        self,
        type: TToken,
        lexeme: str,
        literal: TLiteral | None,
        line: int,
        position: int,
    ) -> None:
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        self.position = position

    def __repr__(self):
        return f"Token(type = {self.type!r}, lexeme = {self.lexeme!r}, literal = {self.literal!r}, line = {self.line!r}, position = {self.position!r})"

    def __str__(self) -> str:
        return f"{self.type} {self.lexeme} {"null" if self.literal is None else self.literal}"
