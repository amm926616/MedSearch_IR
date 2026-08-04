"""
map.py

Mean Average Precision calculation.
"""


def average_precision(
    retrieved_documents,
    relevant_documents
):

    relevant_set = set(
        relevant_documents
    )


    hits = 0
    precision_sum = 0


    for index, document in enumerate(
        retrieved_documents,
        start=1
    ):

        if document in relevant_set:

            hits += 1

            precision_sum += (
                hits / index
            )


    if len(relevant_set) == 0:

        return 0.0


    return (
        precision_sum /
        len(relevant_set)
    )



def mean_average_precision(
    results,
    relevance
):

    scores = []


    for query_id in results:

        ap = average_precision(
            results[query_id],
            relevance[query_id]
        )

        scores.append(ap)


    if len(scores) == 0:

        return 0.0


    return sum(scores) / len(scores)