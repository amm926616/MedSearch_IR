# Indexing Design

## Overview

Indexing is the third stage of the MedSearch IR system.

The purpose of indexing is to organize processed medical documents so that queries can be answered efficiently.

Instead of scanning every document during search, the system creates an inverted index.

---

# Pipeline Position

```
Raw Documents
      |
      ↓
Preprocessing
      |
      ↓
Processed Tokens
      |
      ↓
Inverted Index
      |
      ↓
Ranking
      |
      ↓
Search Results
```

---

# Inverted Index

An inverted index maps terms to the documents containing them.

Traditional document representation:

```
Document → Terms
```

Example:

```
DOC001:
diabetes
blood
glucose
```

Search representation:

```
Term → Documents
```

Example:

```
diabetes:
DOC001
DOC020
DOC100
```

---

# Components

## index_builder.py

Responsible for:

- Reading processed documents
- Creating index entries
- Saving the final index


## inverted_index.py

Responsible for:

- Maintaining term-document relationships
- Adding new terms
- Retrieving postings


## postings.py

Stores document references.

Example:

```
diabetes:
[
DOC001,
DOC020
]
```

---

# Example

Input:

```
DOC001:
diabetes blood glucose


DOC002:
blood pressure
```

Output:

```
{
    "diabetes": [
        "DOC001"
    ],

    "blood": [
        "DOC001",
        "DOC002"
    ],

    "glucose": [
        "DOC001"
    ],

    "pressure": [
        "DOC002"
    ]
}
```

---

# Future Improvements

The index can later support:

- Term frequency
- Document frequency
- TF-IDF weighting
- BM25 ranking
- Positional indexing