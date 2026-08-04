"""
metadata.py

Creates document statistics required for ranking algorithms.
"""


import json
from pathlib import Path


INPUT_FILE = Path(
    "dataset/processed/processed_documents.json"
)


OUTPUT_FILE = Path(
    "dataset/processed/document_metadata.json"
)



def load_documents():

    with INPUT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def build_metadata(documents):

    metadata = {}

    for doc_id, document in documents.items():

        tokens = document["tokens"]

        metadata[doc_id] = {
            "length": len(tokens)
        }


    return metadata



def save_metadata(metadata):

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metadata,
            file,
            indent=4
        )



def run():

    documents = load_documents()

    metadata = build_metadata(
        documents
    )

    save_metadata(
        metadata
    )


    print("=" * 50)
    print("Document Metadata")
    print("=" * 50)

    print(
        f"Documents: {len(metadata)}"
    )

    print(
        f"Saved: {OUTPUT_FILE}"
    )



if __name__ == "__main__":
    run()