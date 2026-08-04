# MedSearch IR
## Medical Information Retrieval System

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Information Retrieval](https://img.shields.io/badge/Domain-Information%20Retrieval-green)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

---

# Overview

MedSearch IR is a medical information retrieval system designed to search and rank healthcare-related documents using classical Information Retrieval techniques.

The project demonstrates the complete search engine pipeline:

- Document collection
- Text preprocessing
- Inverted index construction
- Query processing
- Document ranking
- Retrieval evaluation
- Ranking algorithm comparison

The system was developed as part of an Information Retrieval course project.

---

# Objectives

The main objectives of MedSearch IR are:

- Build a functional medical document search engine
- Apply classical IR algorithms
- Compare different ranking approaches
- Evaluate retrieval performance using standard IR metrics

---

# System Architecture

The system follows a modular Information Retrieval pipeline:

```
Medical Sources

      |
      v

Document Collection

      |
      v

Text Preprocessing

      |
      v

Inverted Index

      |
      v

Query Processing

      |
      v

Ranking

      |
      v

Evaluation
```

Detailed architecture:

```
docs/diagrams/system_architecture.md
```

---

# Features

## Document Collection

The system supports medical document sources including:

- World Health Organization (WHO)
- National Institutes of Health (NIH)
- PubMed
- Centers for Disease Control and Prevention (CDC)

Documents are converted into a unified dataset format.

---

## Text Preprocessing

The preprocessing pipeline performs:

- Text cleaning
- Tokenization
- Normalization
- Stop word handling
- Stemming

Input:

```
raw_documents.json
```

Output:

```
processed_documents.json
```

---

## Indexing

The system builds an inverted index containing:

- Terms
- Document references
- Term frequencies

Generated file:

```
dataset/processed/inverted_index.json
```

---

## Ranking Algorithms

Two ranking models are implemented:

## TF-IDF

Term Frequency-Inverse Document Frequency ranks documents based on the importance of query terms.

## BM25

BM25 improves ranking by considering:

- Term frequency saturation
- Document length normalization
- Query relevance

---

# Evaluation

The system evaluates retrieval performance using:

| Metric | Purpose |
|-|-|
| Precision | Measures retrieved relevance |
| Recall | Measures coverage of relevant documents |
| F1-score | Balance between precision and recall |
| MAP | Measures ranking effectiveness |
| nDCG | Measures ranked result quality |

Evaluation output:

```
results/evaluation_results.csv
```

---

# A/B Testing

The project includes an offline ranking comparison experiment.

Compared systems:

```
System A:
TF-IDF

System B:
BM25
```

Evaluation metric:

```
Mean Average Precision (MAP)
```

Results:

```
results/ab_test_results.csv
```

Example:

| Query | TF-IDF MAP | BM25 MAP | Winner |
|-|-|-|-|
| blood pressure | 1.0 | 1.0 | Tie |
| diabetes | 1.0 | 1.0 | Tie |

The identical scores demonstrate that both ranking algorithms performed successfully on the current evaluation corpus.

---

# Project Structure

```
MedSearch_IR

├── config
│
├── dataset
│   ├── raw
│   ├── processed
│   └── qrels
│
├── docs
│   ├── diagrams
│   └── report_notes
│
├── src
│   ├── collection
│   ├── preprocessing
│   ├── indexing
│   ├── query
│   ├── ranking
│   ├── evaluation
│   └── utils
│
├── tests
│
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/amm926616/MedSearch_IR.git

cd MedSearch_IR
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the System

## 1. Load Dataset

```bash
python -m src.collection.dataset_loader
```

---

## 2. Preprocess Documents

```bash
python -m src.preprocessing.pipeline
```

---

## 3. Build Index

```bash
python -m src.indexing.index_builder
```

---

## 4. Search Documents

Example:

```bash
python -m tests.test_search
```

---

## 5. Evaluate System

```bash
python -m src.evaluation.metrics
```

---

## 6. Run A/B Testing

```bash
python -m src.evaluation.ab_testing
```

---

# Technologies Used

| Technology | Purpose |
|-|-|
| Python | Implementation language |
| JSON | Data storage |
| CSV | Dataset format |
| NLTK | Text processing |
| Git | Version control |

---

# Limitations

The current prototype uses a small manually prepared medical document collection.

Limitations include:

- Limited document size
- Limited query diversity
- No user feedback data
- No semantic search capability

---

# Future Improvements

Potential improvements:

## Larger Medical Corpus

Integrate:

- PubMed datasets
- Europe PMC
- Medical guideline databases

## Semantic Search

Add:

- Word embeddings
- Transformer models
- Vector databases

## Learning-to-Rank

Implement machine learning ranking models using:

- User interaction data
- Click feedback
- Relevance signals

## Personalization

Support:

- User preferences
- Medical specialties
- Search history

---

# Authors

MedSearch IR Project Team

Information Retrieval Course

---

# License

Academic project for educational purposes.
