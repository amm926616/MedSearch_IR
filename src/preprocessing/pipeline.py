"""
pipeline.py

Runs preprocessing on raw_documents.json
"""


import json
from pathlib import Path

from .normalizer import normalize



INPUT_FILE = Path(
    "dataset/processed/raw_documents.json"
)

OUTPUT_FILE = Path(
    "dataset/processed/processed_documents.json"
)


def run():

    with INPUT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        documents = json.load(file)


    processed = {}


    for doc_id, document in documents.items():

        processed[doc_id] = {

            "source": document["source"],

            "title": document["title"],

            "url": document["url"],

            "tokens": normalize(
                document["text"]
            )
        }


    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            processed,
            file,
            indent=4
        )


    print(
        f"Processed {len(processed)} documents"
    )


if __name__ == "__main__":
    run()