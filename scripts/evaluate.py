"""
evaluate.py

Runs MedSearch IR evaluation.

Evaluates search performance using:
- Precision
- Recall
- F1
- MAP
- nDCG
"""
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)


from src.query.search_engine import SearchEngine
from src.evaluation.metrics import (
    evaluate_query,
    save_results
)



QUERY_FILE = (
    "dataset/qrels/queries.json"
)


QREL_FILE = (
    "dataset/qrels/qrels.json"
)



def load_json(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def main():

    queries = load_json(
        QUERY_FILE
    )


    qrels = load_json(
        QREL_FILE
    )


    engine = SearchEngine()


    results = []


    print("=" * 60)
    print("MedSearch IR Evaluation")
    print("=" * 60)



    for query_id, query in queries.items():

        print()

        print(
            f"Evaluating {query_id}: {query}"
        )


        retrieved_results = engine.search(
            query,
            top_k=5
        )


        retrieved_documents = [
            doc_id
            for doc_id, score
            in retrieved_results
        ]


        # Convert old qrels format
        # into graded relevance

        if isinstance(
            qrels[query_id],
            list
        ):

            relevance = {
                doc_id: 1
                for doc_id
                in qrels[query_id]
            }

        else:

            relevance = qrels[query_id]



        scores = evaluate_query(
            retrieved_documents,
            relevance
        )


        scores["query"] = query


        results.append(
            scores
        )



    save_results(
        results
    )


    print()

    print("=" * 60)

    print(
        "Evaluation Complete"
    )

    print(
        "Saved: results/evaluation_results.csv"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()