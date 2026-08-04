import json

from src.query.query_processor import QueryProcessor
from src.ranking.tfidf_ranker import TFIDFRanker



with open(
    "dataset/processed/inverted_index.json"
) as file:

    index = json.load(file)



processor = QueryProcessor()


tokens = processor.process(
    "blood pressure"
)


ranker = TFIDFRanker(
    index,
    total_documents=5
)


results = ranker.rank(
    tokens
)


print("Query:")
print(tokens)


print("\nRanking:")
for doc, score in results:

    print(
        doc,
        score
    )