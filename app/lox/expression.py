from abc import ABC, abstractmethod
from .loxtokens import Token


class Expression(ABC):
    @abstractmethod
    def __str__(self) -> str: ...


class Literal(Expression):
    def __init__(self, value: Token):
        self.value = value
        return super().__init__()

    def __str__(self):
        match self.value.type:
            case "TRUE":
                return "true"
            case "FALSE":
                return "false"
            case "NIL":
                return "nil"
            case _:
                return str(self.value.literal)


class Grouping(Expression):
    def __init__(self, value: Expression):
        self.value = value
        return super().__init__()

    def __str__(self) -> str:
        return f"(group {self.value})"


class UnaryExpression(Expression):
    def __init__(self, operator: Token, right: Expression):
        self.operator = operator
        self.right = right
        return super().__init__()

    def __str__(self) -> str:
        return f"({self.operator.lexeme} {self.right})"


class BinaryExpression(UnaryExpression):
    def __init__(self, left: Expression, operator: Token, right: Expression):
        self.left = left
        return super().__init__(operator, right)

    def __str__(self) -> str:
        return f"({self.operator.lexeme} {self.left} {self.right})"
