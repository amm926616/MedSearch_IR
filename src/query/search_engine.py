"""
search_engine.py

Provides the interactive search interface for MedSearch IR.

Features:
- Query processing
- BM25 ranking
- Top-K retrieval
- Search history logging
"""


import json
from pathlib import Path
from datetime import datetime


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


    HISTORY_FILE = Path(
        "results/logs/search_history.json"
    )



    def __init__(self):

        self.index = self.load_json(
            self.INDEX_FILE
        )

        self.metadata = self.load_json(
            self.METADATA_FILE
        )

        self.documents = self.load_json(
            self.DOCUMENTS_FILE
        )


        self.processor = QueryProcessor()


        self.ranker = BM25Ranker(
            self.index,
            self.metadata,
            len(self.metadata)
        )



    def load_json(self, path):

        with path.open(
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    def generate_snippet(
        self,
        text,
        query_tokens,
        window=120
    ):

        if not text:

            return ""


        text_lower = text.lower()


        positions = []


        for token in query_tokens:

            position = text_lower.find(
                token.lower()
            )

            if position != -1:

                positions.append(
                    position
                )


        if not positions:

            return text[:window] + "..."


        start = max(
            min(positions) - 50,
            0
        )


        end = start + window


        snippet = text[start:end]


        if start > 0:

            snippet = "..." + snippet


        if end < len(text):

            snippet += "..."


        return snippet



    def search(
            self,
            query,
            top_k=5
    ):

        tokens = self.processor.process(
            query
        )

        return self.ranker.rank(
            tokens,
            top_k
        )



    def save_history(
        self,
        query,
        results
    ):


        self.HISTORY_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        history = []


        if self.HISTORY_FILE.exists():

            with self.HISTORY_FILE.open(
                "r",
                encoding="utf-8"
            ) as file:

                history = json.load(file)



        record = {

            "query": query,

            "timestamp":
                datetime.now()
                .strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "results":
                [
                    doc_id
                    for doc_id, score in results
                ]
        }


        history.append(
            record
        )


        with self.HISTORY_FILE.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )



    def display_results(
        self,
        query,
        top_k=5
    ):


        results = self.search(
            query,
            top_k
        )


        self.save_history(
            query,
            results
        )


        print()

        print("=" * 60)

        print(
            f"Search Results for: {query}"
        )

        print("=" * 60)



        if not results:

            print(
                "No relevant medical documents found."
            )

            return

        query_terms = query.split()

        for rank, (doc_id, score) in enumerate(
                results,
                start=1
        ):
            document = self.metadata.get(
                doc_id
            )

            full_document = self.documents.get(
                doc_id
            )

            snippet = self.generate_snippet(
                full_document.get("text", ""),
                query_terms
            )

            print()

            print(
                f"{rank}. {document['title']}"
            )

            print()

            print(
                f"{snippet}"
            )

            print()

            print(
                f"Source : {document['source']}"
            )

            print(
                f"Score  : {score:.4f}"
            )

            print(
                f"URL    : {document['url']}"
            )

            print(
                "-" * 60
            )