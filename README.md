# 🩺 MedSearch IR

> **A Modular Healthcare Information Retrieval System**
>
> **University of the People – CS 3308 Information Retrieval**
>
> Group Project: Designing and Evaluating a Real-World Information Retrieval System

---

## Overview

**MedSearch IR** is a modular healthcare document retrieval system that demonstrates the complete lifecycle of a classical Information Retrieval (IR) system—from document collection and preprocessing to indexing, ranking, and evaluation.

The project is inspired by the architecture of modern search engines while remaining lightweight enough to be implemented within an academic setting. It emphasizes **modularity, reproducibility, and explainability**, making it suitable for studying core IR concepts and evaluating retrieval performance.

The implementation focuses on traditional IR techniques such as:

- Inverted Indexing
- TF-IDF Ranking
- BM25 Ranking
- Precision & Recall
- MAP (Mean Average Precision)
- nDCG (Normalized Discounted Cumulative Gain)

Future extensions such as Dense Retrieval, Learning-to-Rank, and Retrieval-Augmented Generation (RAG) are discussed as potential improvements but are intentionally excluded from the implementation scope.

---

# System Architecture

MedSearch IR is divided into two major pipelines.

## Offline Indexing Pipeline

Responsible for preparing searchable data.

```
Medical Documents
        │
        ▼
Document Collection
        │
        ▼
Text Preprocessing
        │
        ▼
Inverted Index Construction
        │
        ▼
Index Storage
(postings.json, metadata.json)
```

---

## Online Search Pipeline

Responsible for answering user queries.

```
User Query
      │
      ▼
Query Processing
      │
      ▼
Retrieval & Ranking
(TF-IDF / BM25)
      │
      ▼
Ranked Documents
      │
      ▼
Evaluation Framework
```

---

# Project Components

## 1. Healthcare Document Collection

Builds the searchable medical corpus from public healthcare resources.

Possible data sources include:

- PubMed Abstracts
- NIH
- WHO
- Public medical datasets

**Output**

```
raw_documents.json
```

---

## 2. Text Preprocessing Pipeline

Converts raw text into normalized searchable tokens.

Pipeline:

- Text cleaning
- Lowercasing
- Tokenization
- Stopword removal
- Stemming / Lemmatization

---

## 3. Inverted Index Construction

Creates the core search structure that maps:

```
Term
    ↓
Documents
```

Outputs:

```
postings.json
metadata.json
```

---

## 4. Query Processing

Processes user queries using the same preprocessing pipeline applied during indexing to ensure consistent document matching.

---

## 5. Retrieval & Ranking Engine

Implements two ranking models.

### Baseline

- TF-IDF

### Advanced

- BM25

The ranking engine returns the Top-K most relevant healthcare documents for each query.

---

## 6. Evaluation Framework

Measures retrieval effectiveness using standard IR metrics.

Implemented metrics include:

- Precision@K
- Recall@K
- F1 Score
- MAP
- nDCG

Evaluation uses benchmark queries and relevance judgments (qrels).

---

## 7. Visualization & Reporting

Generates tables and figures used in the final project report, including:

- Ranking comparisons
- Evaluation charts
- Performance summaries
- Architecture diagrams

---

# Repository Structure

```
MedSearch_IR/

├── dataset/
│
├── src/
│   ├── collection/
│   ├── preprocessing/
│   ├── indexing/
│   ├── ranking/
│   └── evaluation/
│
├── docs/
│
├── results/
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3 |
| Data Processing | Pandas, NumPy |
| NLP | NLTK |
| Data Collection | Requests, BeautifulSoup |
| Storage | JSON |
| Ranking | TF-IDF, BM25 |
| Visualization | Matplotlib |
| Testing | Pytest (optional) |

---

# Getting Started

## Clone the Repository

```bash
git clone https://github.com/<username>/MedSearch_IR.git

cd MedSearch_IR
```

---

## Create Virtual Environment

Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Build the Index

```bash
python main.py index
```

---

## Search the Corpus

```bash
python main.py search
```

---

# Development Roadmap

The project is implemented following the priority order defined in the project blueprint.

| Phase | Status |
|---------|--------|
| Repository Setup | ✅ |
| Healthcare Document Collection | ⏳ |
| Text Preprocessing | ⏳ |
| Inverted Index Construction | ⏳ |
| Query Processing | ⏳ |
| TF-IDF Ranking | ⏳ |
| BM25 Ranking | ⏳ |
| Evaluation Metrics | ⏳ |
| Visualization | ⏳ |
| Documentation | ⏳ |

---

# Outputs

The system generates several artifacts during execution.

```
raw_documents.json
postings.json
metadata.json

evaluation_results.csv

results/
charts/
```

---

# Future Work

Although not implemented in this project, the architecture is designed to support future research directions including:

- Dense Retrieval
- Sentence Embeddings
- BERT Retrieval
- ColBERT
- Learning-to-Rank
- Conversational Search
- Retrieval-Augmented Generation (RAG)

---

# Contributors

This project is developed collaboratively as part of the **CS 3308 Information Retrieval Group Project** at the **University of the People**.

---

# License

This repository is intended for educational and academic purposes.

---

## Acknowledgements

This project draws inspiration from classical Information Retrieval systems and modern search engine architectures, incorporating concepts such as inverted indexing, probabilistic ranking, and retrieval evaluation commonly used in both academia and industry.