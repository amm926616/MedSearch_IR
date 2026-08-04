"""
ab_testing.py

Offline A/B testing framework for comparing
TF-IDF and BM25 ranking algorithms.
"""


import csv
from pathlib import Path


from .metrics import evaluate_query



def compare_rankings(
    tfidf_results,
    bm25_results,
    relevance
):

    """
    Compare two ranking approaches.
    """


    tfidf_scores = evaluate_query(
        tfidf_results,
        relevance
    )


    bm25_scores = evaluate_query(
        bm25_results,
        relevance
    )


    return {

        "tfidf": tfidf_scores,

        "bm25": bm25_scores
    }




def determine_winner(
    tfidf_score,
    bm25_score
):

    """
    Determine better ranking algorithm.
    """

    if tfidf_score > bm25_score:

        return "TF-IDF"


    elif bm25_score > tfidf_score:

        return "BM25"


    else:

        return "Tie"




def save_results(results):

    output = Path(
        "results/ab_test_results.csv"
    )


    output.parent.mkdir(
        exist_ok=True
    )


    with output.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:


        writer = csv.DictWriter(
            file,
            fieldnames=[
                "query",
                "tfidf_MAP",
                "bm25_MAP",
                "winner"
            ]
        )


        writer.writeheader()


        writer.writerows(
            results
        )




def main():


    """
    Example offline A/B experiment.
    """


    experiments = {


        "blood pressure":

        {

            "tfidf":

            [

                "DOC0002",

                "DOC0003"

            ],


            "bm25":

            [

                "DOC0002",

                "DOC0003"

            ],


            "relevance":

            {

                "DOC0002": 2,

                "DOC0003": 1

            }

        },



        "diabetes":

        {

            "tfidf":

            [

                "DOC0003"

            ],


            "bm25":

            [

                "DOC0003"

            ],


            "relevance":

            {

                "DOC0003": 2

            }

        }

    }



    results = []



    for query, experiment in experiments.items():


        comparison = compare_rankings(

            experiment["tfidf"],

            experiment["bm25"],

            experiment["relevance"]

        )


        tfidf_map = comparison["tfidf"]["MAP"]

        bm25_map = comparison["bm25"]["MAP"]



        winner = determine_winner(

            tfidf_map,

            bm25_map

        )



        results.append(

            {

                "query": query,

                "tfidf_MAP": tfidf_map,

                "bm25_MAP": bm25_map,

                "winner": winner

            }

        )



    save_results(results)



    print("=" * 50)

    print("A/B Testing Complete")

    print(
        "Saved: results/ab_test_results.csv"
    )

    print("=" * 50)




if __name__ == "__main__":

    main()