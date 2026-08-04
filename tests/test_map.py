from src.evaluation.map import average_precision



retrieved = [
    "DOC0002",
    "DOC0005",
    "DOC0003"
]


relevant = [
    "DOC0002",
    "DOC0003"
]


score = average_precision(
    retrieved,
    relevant
)


print(
    "Average Precision:",
    score
)