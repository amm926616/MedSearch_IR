"""
f1.py

Calculates F1 score.
"""


def f1_score(
    precision,
    recall
):


    if precision + recall == 0:

        return 0.0


    return (
        2 *
        (
            precision *
            recall
        )
        /
        (
            precision +
            recall
        )
    )