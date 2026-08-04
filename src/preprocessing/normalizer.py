"""
normalizer.py

Controls the complete text normalization process.
"""


from .cleaner import clean_text
from .tokenizer import tokenize
from .stopwords import remove_stopwords
from .stemmer import stem_tokens


def normalize(text):

    text = clean_text(text)

    tokens = tokenize(text)

    tokens = remove_stopwords(tokens)

    tokens = stem_tokens(tokens)

    return tokens