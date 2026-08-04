"""
recall.py

Calculates recall metric.
"""


def recall(
    retrieved_documents,
    relevant_documents
):


    if len(relevant_documents) == 0:

        return 0.0



    retrieved_set = set(
        retrieved_documents
    )


    relevant_set = set(
        relevant_documents
    )


    relevant_retrieved = (
        retrieved_set
        &
        relevant_set
    )


    return (
        len(relevant_retrieved)
        /
        len(relevant_set)
    )