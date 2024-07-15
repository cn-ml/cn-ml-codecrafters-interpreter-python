from ..lexing.error import ParseException
from .tokens import Token
from .grammar import Grammar


class Parser[TToken, TLiteral, TExpression](
    Grammar[Token[TToken, TLiteral], TExpression]
):
    def match_any(self, *expected: TToken):
        for exp in expected:
            if (matched := self.match(exp)) is not None:
                return matched
        return None

    def match(self, expected: TToken):
        if self.exhausted():
            return None
        if (token := self.peek()) is not None and token.type == expected:
            return self.advance()
        return None

    def consume(self, expected: TToken, message: str):
        if self.match(expected) is not None:
            return
        raise ParseException(message)
