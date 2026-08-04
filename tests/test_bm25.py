import json

from src.query.query_processor import QueryProcessor
from src.ranking.bm25_ranker import BM25Ranker



with open(
    "dataset/processed/inverted_index.json"
) as file:

    index = json.load(file)



with open(
    "dataset/processed/document_metadata.json"
) as file:

    metadata = json.load(file)



processor = QueryProcessor()


query = processor.process(
    "blood pressure"
)


ranker = BM25Ranker(
    index,
    metadata,
    len(metadata)
)


results = ranker.rank(query)


print("Query:")
print(query)


print("\nBM25 Ranking:")

for doc, score in results:

    print(
        doc,
        score
    )