"""
stopwords.py

Removes common English words.
"""


STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "of",
    "and",
    "to",
    "in",
    "for",
    "with",
    "on",
}


def remove_stopwords(tokens):
    """
    Remove words with low information value.
    """

    return [
        token
        for token in tokens
        if token not in STOPWORDS
    ]