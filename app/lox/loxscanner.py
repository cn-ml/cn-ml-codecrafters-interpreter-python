from ..lexing import Scanner
from .loxtokens import (
    KEYWORD_TOKENS,
    SINGLE_CHAR_TOKENS,
    WITH_EQUALS_SIGN,
    LoxLiteral,
    LoxTokenType,
)


class LoxScanner(Scanner[LoxTokenType, LoxLiteral]):
    def _make_eof(self):
        return self._make("EOF")

    def scan_token(self):
        c = self._advance()
        if c == "/":
            if self.match("/"):
                while self._peek() != "\n" and not self.exhausted():
                    self._advance()
            else:
                return self._make("SLASH")
        elif (type := SINGLE_CHAR_TOKENS.get(c)) is not None:
            return self._make(
                with_equals
                if (with_equals := WITH_EQUALS_SIGN.get(type)) and self.match("=")
                else type
            )
        elif c.isspace():
            if c == "\n":
                self._reset_line()
        elif c.isdigit():
            return self._digit()
        elif is_alpha(c):
            return self._identifier()
        elif c == '"':
            return self._string()
        else:
            raise self._scan_error(f"Unexpected character: {c}")

    def _identifier(self):
        while is_alnum(self._peek()):
            self._advance()
        lexeme = self._lexeme()
        if (keyword := KEYWORD_TOKENS.get(lexeme)) is not None:
            return self._make(keyword)
        return self._make("IDENTIFIER")

    def _string(self):
        while (peek := self._peek()) != '"' and not self.exhausted():
            if peek == "\n":
                self._reset_line()
            self._advance()
        if self.exhausted():
            raise self._scan_error("Unterminated string.")
        self._advance()  # closing symbol
        return self._make("STRING", lambda x: x.strip('"'))

    def _digit(self):
        while (peek := self._peek()).isdigit():
            self._advance()
        if peek == "." and self._peek_ahead(1).isdigit():
            self._advance()
            while self._peek().isdigit():
                self._advance()
        return self._make("NUMBER", float)


def is_alpha(character: str):
    return character.isalpha() or character == "_"


def is_alnum(character: str):
    return character.isalnum() or character == "_"
