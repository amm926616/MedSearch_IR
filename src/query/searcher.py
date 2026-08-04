"""
searcher.py

Retrieves documents from the inverted index.
"""


import json
from pathlib import Path


class Searcher:


    def __init__(self, index_path):

        self.index_path = Path(index_path)

        self.index = self.load_index()



    def load_index(self):

        with self.index_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)



    def search(self, query_tokens):

        results = set()


        for token in query_tokens:

            if token in self.index:

                documents = self.index[token]

                results.update(
                    documents.keys()
                )

        return list(results)