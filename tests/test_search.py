from src.query.query_processor import QueryProcessor
from src.query.searcher import Searcher



processor = QueryProcessor()


query = "blood pressure"


tokens = processor.process(query)


print("Processed query:")
print(tokens)



searcher = Searcher(
    "dataset/processed/inverted_index.json"
)


results = searcher.search(tokens)


print("\nResults:")
print(results)