from src.evaluation.precision import precision
from src.evaluation.recall import recall
from src.evaluation.f1 import f1_score



retrieved = [
    "DOC0002",
    "DOC0003",
    "DOC0005"
]


relevant = [
    "DOC0002",
    "DOC0003"
]


p = precision(
    retrieved,
    relevant
)


r = recall(
    retrieved,
    relevant
)


f1 = f1_score(
    p,
    r
)


print("Precision:", p)

print("Recall:", r)

print("F1:", f1)