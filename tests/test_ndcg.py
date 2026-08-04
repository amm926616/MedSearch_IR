from src.evaluation.ndcg import ndcg



retrieved = [

    "DOC0005",

    "DOC0002",

    "DOC0003"

]


relevance = {

    "DOC0002": 2,

    "DOC0003": 1,

    "DOC0005": 0

}



score = ndcg(
    retrieved,
    relevance
)


print(
    "nDCG:",
    score
)