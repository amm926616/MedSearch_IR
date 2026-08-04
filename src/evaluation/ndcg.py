"""
ndcg.py

Normalized Discounted Cumulative Gain calculation.
"""


import math



def dcg(relevances):

    score = 0


    for index, relevance in enumerate(
        relevances
    ):

        position = index + 1


        score += (
            relevance /
            math.log2(position + 1)
        )


    return score



def ndcg(
    retrieved_documents,
    relevance_scores,
    k=None
):


    if k:

        retrieved_documents = (
            retrieved_documents[:k]
        )


    retrieved_relevances = []


    for document in retrieved_documents:

        retrieved_relevances.append(
            relevance_scores.get(
                document,
                0
            )
        )


    actual_dcg = dcg(
        retrieved_relevances
    )


    ideal_relevances = sorted(
        relevance_scores.values(),
        reverse=True
    )


    ideal_dcg = dcg(
        ideal_relevances
    )


    if ideal_dcg == 0:

        return 0.0


    return actual_dcg / ideal_dcg