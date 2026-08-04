"""
main.py

Entry point for the MedSearch IR System.
"""

from src.collection.dataset_loader import DatasetLoader
from src.preprocessing.pipeline import run as preprocess
from src.indexing.index_builder import run as build_index

from src.evaluation.metrics import main as evaluate
from src.evaluation.ab_testing import main as ab_test


class MedSearchIR:

    def banner(self):

        print("=" * 60)
        print("        MedSearch IR")
        print(" Medical Information Retrieval System")
        print("=" * 60)

    def menu(self):

        print()
        print("1. Load Dataset")
        print("2. Preprocess Documents")
        print("3. Build Inverted Index")
        print("4. Search Documents")
        print("5. Evaluate System")
        print("6. A/B Testing")
        print("0. Exit")
        print()

    def run(self):

        while True:

            self.banner()
            self.menu()

            choice = input("Select option: ").strip()

            if choice == "1":

                loader = DatasetLoader(
                    csv_path="dataset/raw/medical_articles.csv",
                    output_path="dataset/processed/raw_documents.json",
                )

                loader.run()

            elif choice == "2":

                preprocess()

            elif choice == "3":

                build_index()


            elif choice == "4":

                from src.query.search_engine import SearchEngine

                engine = SearchEngine()

                while True:

                    print()

                    query = input(

                        "Search query (blank to return): "

                    ).strip()

                    if query == "":
                        break

                    engine.display_results(

                        query

                    )

            elif choice == "5":

                evaluate()

            elif choice == "6":

                ab_test()

            elif choice == "0":

                print("\nGoodbye.\n")
                break

            else:

                print("\nInvalid option.\n")

            input("\nPress Enter to continue...")


def main():

    app = MedSearchIR()

    app.run()


if __name__ == "__main__":
    main()