from abc import ABC, abstractmethod
from typing import Iterable, Sequence


class Grammar[TInput, TOutput](ABC):
    def __init__(self, source: Sequence[TInput]) -> None:
        self.source = source
        self.current = 0

    def exhausted(self, offset: int = 0):
        position = self.current + offset
        return position < 0 or self.current + offset >= len(self.source)

    def peek(self, offset: int = 0):
        return None if self.exhausted(offset) else self.source[self.current + offset]

    def advance(self):
        self.current = (current := self.current) + 1
        return self.source[current]

    @abstractmethod
    def execute(self) -> Iterable[TOutput]: ...
