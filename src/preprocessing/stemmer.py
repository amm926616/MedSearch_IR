"""
stemmer.py

Reduces words to their root forms.
"""


from nltk.stem import PorterStemmer


stemmer = PorterStemmer()


def stem_tokens(tokens):
    """
    Apply stemming.
    """

    return [
        stemmer.stem(token)
        for token in tokens
    ]