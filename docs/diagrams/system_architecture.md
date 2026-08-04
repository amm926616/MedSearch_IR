# MedSearch IR System Architecture

## Overview

The MedSearch IR system follows a traditional Information Retrieval pipeline consisting of document collection, preprocessing, indexing, retrieval, ranking, and evaluation components.

The architecture is designed as a modular pipeline where each component has a specific responsibility.

---
# System Pipeline

                     Medical Sources

                          |
                          |
                          v

                +----------------+
                |  Collection    |
                |                |
                | dataset_loader |
                | crawler        |
                +----------------+

                          |
                          |
                          v

                raw_documents.json


                          |
                          |
                          v


                +----------------+
                | Preprocessing  |
                |                |
                | Cleaning       |
                | Tokenization   |
                | Normalization  |
                | Stemming       |
                +----------------+

                          |
                          |
                          v


             processed_documents.json


                          |
                          |
                          v


                +----------------+
                |   Indexing     |
                |                |
                | Inverted Index |
                | Metadata       |
                +----------------+

                          |
                          |
                          v


             inverted_index.json


                          |
                          |
                          v


                     User Query

                          |
                          |
                          v


                +----------------+
                | Query Process  |
                |                |
                | Tokenization   |
                | Normalization  |
                +----------------+

                          |
                          |
                          v


                +----------------+
                |   Ranking      |
                |                |
                | TF-IDF         |
                | BM25           |
                +----------------+

                          |
                          |
                          v


                 Ranked Documents


                          |
                          |
                          v


                +----------------+
                |  Evaluation    |
                |                |
                | Precision      |
                | Recall         |
                | F1             |
                | MAP            |
                | nDCG           |
                +----------------+


                          |
                          |
                          v


                Performance Report

---

# Component Description

| Component | Responsibility |
|---|---|
| Collection | Acquires and standardizes medical documents |
| Preprocessing | Cleans and transforms raw text |
| Indexing | Builds searchable data structures |
| Query Processing | Converts user queries into searchable terms |
| Ranking | Calculates document relevance |
| Evaluation | Measures retrieval effectiveness |

---

# Data Flow

The complete data transformation is:

```

medical_articles.csv

```
    ↓
```

raw_documents.json

```
    ↓
```

processed_documents.json

```
    ↓
```

inverted_index.json

```
    ↓
```

Ranked Search Results

```
    ↓
```

Evaluation Results.csv

```

---

# Design Principles

The system follows several software engineering principles:

## Modularity

Each component is independent and can be improved separately.

Example:

BM25 can be replaced without modifying preprocessing or indexing.

---

## Single Responsibility

Each module performs one specific task.

Examples:

- tokenizer.py → token generation
- stemmer.py → word normalization
- index_builder.py → index creation
- bm25_ranker.py → ranking

---

## Extensibility

The architecture allows future improvements:

- additional medical sources
- machine learning ranking models
- semantic search
- user personalization
- larger datasets

---

