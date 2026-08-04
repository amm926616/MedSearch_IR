"""
cleaner.py

Responsible for removing unnecessary characters
and cleaning raw text.
"""


import re


def clean_text(text: str) -> str:
    """
    Clean raw document text.

    Steps:
    - lowercase text
    - remove special characters
    - remove extra spaces
    """

    text = text.lower()

    text = re.sub(
        r"[^a-z\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()