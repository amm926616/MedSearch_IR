"""
search_engine.py

Provides the search interface for MedSearch IR.
"""

import json
from pathlib import Path

from src.query.query_processor import QueryProcessor
from src.ranking.bm25_ranker import BM25Ranker


class SearchEngine:

    INDEX_FILE = Path(
        "dataset/processed/inverted_index.json"
    )

    METADATA_FILE = Path(
        "dataset/processed/document_metadata.json"
    )

    DOCUMENTS_FILE = Path(
        "dataset/processed/processed_documents.json"
    )


    def __init__(self):

        # Load inverted index
        with self.INDEX_FILE.open(
            "r",
            encoding="utf-8"
        ) as file:

            self.index = json.load(file)


        # Load metadata
        with self.METADATA_FILE.open(
            "r",
            encoding="utf-8"
        ) as file:

            self.metadata = json.load(file)


        # Load documents for displaying results
        with self.DOCUMENTS_FILE.open(
            "r",
            encoding="utf-8"
        ) as file:

            self.documents = json.load(file)


        self.processor = QueryProcessor()


        self.ranker = BM25Ranker(
            self.index,
            self.metadata,
            len(self.metadata)
        )


    def search(self, query):

        tokens = self.processor.process(
            query
        )

        results = self.ranker.rank(
            tokens
        )

        return results


    def display_results(self, query):

        results = self.search(query)


        print()
        print("=" * 60)
        print("Search Results")
        print("=" * 60)


        if not results:

            print("No documents found.")

            return



        for rank, (doc_id, score) in enumerate(
            results,
            start=1
        ):

            document = self.documents[doc_id]


            print()
            print(f"{rank}.")
            print(
                f"Title  : {document['title']}"
            )
            print(
                f"Source : {document['source']}"
            )
            print(
                f"Score  : {score:.4f}"
            )
            print(
                f"URL    : {document['url']}"
            )

            print("-" * 60)