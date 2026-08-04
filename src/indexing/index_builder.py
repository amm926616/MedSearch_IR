"""
index_builder.py

Builds an inverted index from processed medical documents.
"""


import json
from pathlib import Path

from .inverted_index import InvertedIndex
from .metadata import build_metadata, save_metadata


INPUT_FILE = Path(
    "dataset/processed/processed_documents.json"
)

OUTPUT_FILE = Path(
    "dataset/processed/inverted_index.json"
)


def load_documents():

    with INPUT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def build_index(documents):

    index = InvertedIndex()

    for doc_id, document in documents.items():

        tokens = document["tokens"]

        for token in tokens:

            index.add_term(
                token,
                doc_id
            )

    return index



def save_index(index):

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            index.to_dict(),
            file,
            indent=4
        )



def run():

    print("=" * 50)
    print("Building Search Index")
    print("=" * 50)


    documents = load_documents()


    # Build inverted index

    index = build_index(
        documents
    )


    save_index(
        index
    )


    # Build document metadata

    metadata = build_metadata(
        documents
    )


    save_metadata(
        metadata
    )


    print()

    print(
        f"Documents indexed: {len(documents)}"
    )


    print(
        f"Unique terms: {len(index.index)}"
    )


    print(
        f"Metadata documents: {len(metadata)}"
    )


    print()

    print(
        "Saved:"
    )

    print(
        f"- {OUTPUT_FILE}"
    )

    print(
        "- dataset/processed/document_metadata.json"
    )


if __name__ == "__main__":
    run()