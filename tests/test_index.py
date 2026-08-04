from src.indexing.inverted_index import InvertedIndex


index = InvertedIndex()


index.add_term(
    "diabetes",
    "DOC0001"
)

index.add_term(
    "blood",
    "DOC0001"
)

index.add_term(
    "blood",
    "DOC0002"
)


print(index.to_dict())

print(
    index.search("blood")
)