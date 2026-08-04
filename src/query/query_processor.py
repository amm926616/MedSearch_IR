"""
query_processor.py

Processes user search queries using the same
preprocessing pipeline used for documents.
"""


from src.preprocessing.normalizer import normalize



class QueryProcessor:
    """
    Converts raw user queries into searchable tokens.
    """


    def process(self, query: str):

        return normalize(query)