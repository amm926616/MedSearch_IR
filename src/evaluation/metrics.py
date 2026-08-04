"""
metrics.py

Runs complete IR evaluation pipeline.

Calculates:
- Precision
- Recall
- F1
- MAP
- nDCG

Exports results to CSV.
"""


import csv
from pathlib import Path

from .precision import precision
from .recall import recall
from .f1 import f1_score
from .map import average_precision
from .ndcg import ndcg



def evaluate_query(
    retrieved,
    relevant_scores
):

    relevant_documents = list(
        relevant_scores.keys()
    )


    p = precision(
        retrieved,
        relevant_documents
    )


    r = recall(
        retrieved,
        relevant_documents
    )


    f1 = f1_score(
        p,
        r
    )


    ap = average_precision(
        retrieved,
        relevant_documents
    )


    n = ndcg(
        retrieved,
        relevant_scores
    )


    return {
        "precision": p,
        "recall": r,
        "f1": f1,
        "MAP": ap,
        "nDCG": n
    }



def save_results(results):

    output = Path(
        "results/evaluation_results.csv"
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
                "precision",
                "recall",
                "f1",
                "MAP",
                "nDCG"
            ]
        )


        writer.writeheader()


        writer.writerows(results)



def main():

    test_queries = {

        "blood pressure": {

            "retrieved": [
                "DOC0002",
                "DOC0003"
            ],

            "relevance": {

                "DOC0002": 2,

                "DOC0003": 1
            }
        },


        "diabetes": {

            "retrieved": [
                "DOC0003"
            ],

            "relevance": {

                "DOC0003": 2
            }
        },


        "influenza": {

            "retrieved": [
                "DOC0004"
            ],

            "relevance": {

                "DOC0004": 2
            }
        }
    }



    results = []


    for query, data in test_queries.items():

        scores = evaluate_query(
            data["retrieved"],
            data["relevance"]
        )


        scores["query"] = query


        results.append(
            scores
        )


    save_results(
        results
    )


    print("=" * 50)

    print(
        "Evaluation Complete"
    )

    print(
        "Saved: results/evaluation_results.csv"
    )

    print("=" * 50)



if __name__ == "__main__":

    main()