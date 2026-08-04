"""
pipeline_check.py

Checks whether the MedSearch IR pipeline
has generated the required files before search.
"""


from pathlib import Path



REQUIRED_FILES = [

    Path(
        "dataset/processed/raw_documents.json"
    ),

    Path(
        "dataset/processed/processed_documents.json"
    ),

    Path(
        "dataset/processed/inverted_index.json"
    ),

    Path(
        "dataset/processed/document_metadata.json"
    )

]



def check_pipeline():

    missing = []


    for file in REQUIRED_FILES:

        if not file.exists():

            missing.append(
                str(file)
            )


    return missing



def display_pipeline_error(missing):

    print()

    print("=" * 60)

    print(
        "MedSearch IR is not ready."
    )

    print("=" * 60)


    print()

    print(
        "Missing files:"
    )


    for file in missing:

        print(
            f"- {file}"
        )


    print()

    print(
        "Please run the indexing pipeline:"
    )


    print()

    print(
        "python scripts/crawl.py"
    )

    print(
        "python scripts/load_dataset.py"
    )

    print(
        "python scripts/preprocess.py"
    )

    print(
        "python scripts/build_index.py"
    )

    print()