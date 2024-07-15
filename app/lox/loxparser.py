from typing import Callable, Iterable

from app.lexing.error import ParseException
from .expression import BinaryExpression, Expression, Grouping, Literal, UnaryExpression
from ..lexing import Parser
from .loxtokens import LoxLiteral, LoxTokenType


class LoxParser(Parser[LoxTokenType, LoxLiteral, Expression]):
    def execute(self) -> Iterable[Expression]:
        yield self.equality()

    def la(self, read: Callable[[], Expression], *infix: LoxTokenType):
        expr = read()
        while (matched := self.match_any(*infix)) is not None:
            right = read()
            expr = BinaryExpression(expr, matched, right)
        return expr

    def expression(self):
        return self.equality()

    def equality(self):
        return self.la(self.comparison, "EQUAL_EQUAL", "BANG_EQUAL")

    def comparison(self):
        return self.la(self.term, "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL")

    def term(self):
        return self.la(self.factor, "MINUS", "PLUS")

    def factor(self):
        return self.la(self.unary, "STAR", "SLASH")

    def unary(self) -> Expression:
        if (matched := self.match_any("BANG", "MINUS")) is not None:
            right = self.unary()
            return UnaryExpression(matched, right)
        return self.primary()

    def primary(self) -> Expression:
        if matched := self.match("FALSE"):
            return Literal(matched)
        if matched := self.match("TRUE"):
            return Literal(matched)
        if matched := self.match("NIL"):
            return Literal(matched)
        if (matched := self.match_any("NUMBER", "STRING")) is not None:
            return Literal(matched)
        if self.match("LEFT_PAREN"):
            expr = self.expression()
            self.consume("RIGHT_PAREN", "Expect ')' after expression.")
            return Grouping(expr)
        raise ParseException("No parser rule!")
