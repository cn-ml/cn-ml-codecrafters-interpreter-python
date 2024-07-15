from typing import Literal, cast, get_args

SingleCharacterToken = Literal[
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "COMMA",
    "DOT",
    "MINUS",
    "PLUS",
    "SEMICOLON",
    "SLASH",
    "STAR",
    "BANG",
    "EQUAL",
    "GREATER",
    "LESS",
]

SINGLE_CHAR_TOKENS: dict[str, SingleCharacterToken] = {
    "(": "LEFT_PAREN",
    ")": "RIGHT_PAREN",
    "{": "LEFT_BRACE",
    "}": "RIGHT_BRACE",
    ",": "COMMA",
    ".": "DOT",
    "-": "MINUS",
    "+": "PLUS",
    ";": "SEMICOLON",
    "/": "SLASH",
    "*": "STAR",
    "!": "BANG",
    "=": "EQUAL",
    ">": "GREATER",
    "<": "LESS",
}

TwoCharToken = Literal[
    "BANG_EQUAL",
    "EQUAL_EQUAL",
    "GREATER_EQUAL",
    "LESS_EQUAL",
]

WITH_EQUALS_SIGN: dict[SingleCharacterToken, TwoCharToken] = {
    "BANG": "BANG_EQUAL",
    "EQUAL": "EQUAL_EQUAL",
    "GREATER": "GREATER_EQUAL",
    "LESS": "LESS_EQUAL",
}

KeywordToken = Literal[
    "AND",
    "CLASS",
    "ELSE",
    "FALSE",
    "FUN",
    "FOR",
    "IF",
    "NIL",
    "OR",
    "PRINT",
    "RETURN",
    "SUPER",
    "THIS",
    "TRUE",
    "VAR",
    "WHILE",
    "EOF",
]

_keywords = cast(tuple[KeywordToken, ...], get_args(KeywordToken))
KEYWORD_TOKENS = dict((cast(str, token.lower()), token) for token in _keywords)

LiteralToken = Literal[
    "IDENTIFIER",
    "STRING",
    "NUMBER",
]

LoxToken = Literal[SingleCharacterToken, TwoCharToken, LiteralToken, KeywordToken]

LoxLiteral = str | int | float
