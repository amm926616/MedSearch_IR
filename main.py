"""
MedSearch IR

Main application entry point.

Provides interactive medical search
using the pre-built inverted index.
"""


from src.query.search_engine import SearchEngine

from src.utils.pipeline_check import (
    check_pipeline,
    display_pipeline_error
)


def banner():

    print("=" * 60)
    print("        MedSearch IR System")
    print("        Medical Information Retrieval Engine")
    print("=" * 60)



def launch_search():

    print("\nMedical Search Engine Ready")

    engine = SearchEngine()


    while True:

        print()

        query = input(
            "Medical Search > "
        )


        if query.lower() in [
            "exit",
            "quit",
            "q"
        ]:

            print(
                "Closing MedSearch IR."
            )

            break


        engine.display_results(
            query
        )



def main():

    banner()


    missing = check_pipeline()


    if missing:

        display_pipeline_error(
            missing
        )

        return


    launch_search()



if __name__ == "__main__":
    main()