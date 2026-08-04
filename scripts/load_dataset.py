"""
load_dataset.py

Loads crawled medical articles into the IR processing pipeline.

Converts:
dataset/raw/medical_articles.csv

into:

dataset/processed/raw_documents.json
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)

from src.collection.dataset_loader import DatasetLoader


def main():

    loader = DatasetLoader(
        csv_path="dataset/raw/medical_articles.csv",
        output_path="dataset/processed/raw_documents.json",
    )

    loader.run()



if __name__ == "__main__":
    main()