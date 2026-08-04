"""
tokenizer.py

Splits cleaned text into tokens.
"""


def tokenize(text: str) -> list[str]:
    """
    Convert text into individual words.
    """

    return text.split()