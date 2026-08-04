"""
dataset_loader.py

Loads the standardized medical_articles.csv dataset and converts it into
raw_documents.json for the rest of the Information Retrieval pipeline.

Author: MedSearch IR Team
"""

from pathlib import Path
import csv
import json


class DatasetLoader:
    """
    Loads a medical dataset stored in CSV format and exports it as JSON.
    """

    REQUIRED_COLUMNS = ["id", "source", "title", "url", "text"]

    def __init__(self, csv_path: str, output_path: str):
        self.csv_path = Path(csv_path)
        self.output_path = Path(output_path)

    def validate(self):
        """
        Validate the CSV file before processing.
        """

        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.csv_path}"
            )

        with self.csv_path.open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                raise ValueError("CSV file has no header.")

            missing = [
                column
                for column in self.REQUIRED_COLUMNS
                if column not in reader.fieldnames
            ]

            if missing:
                raise ValueError(
                    f"Missing required columns: {missing}"
                )

    def load(self):
        """
        Read the CSV file and convert it into a dictionary.
        """

        documents = {}

        with self.csv_path.open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:

                doc_id = row["id"].strip()

                documents[doc_id] = {
                    "source": row["source"].strip(),
                    "title": row["title"].strip(),
                    "url": row["url"].strip(),
                    "text": row["text"].strip(),
                }

        return documents

    def save(self, documents):
        """
        Save the documents as formatted JSON.
        """

        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.output_path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                documents,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def run(self):
        """
        Execute the complete loading pipeline.
        """

        self.validate()

        documents = self.load()

        self.save(documents)

        print("=" * 50)
        print("Dataset Loader")
        print("=" * 50)
        print(f"Loaded documents : {len(documents)}")
        print(f"Output           : {self.output_path}")
        print("Done.")


def main():

    loader = DatasetLoader(
        csv_path="dataset/raw/medical_articles.csv",
        output_path="dataset/processed/raw_documents.json",
    )

    loader.run()


if __name__ == "__main__":
    main()