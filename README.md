# MedSearch IR

> **CS 3308 – Information Retrieval**  
> **Group Project:** Designing and Evaluating a Real-World Information Retrieval System

## Overview

**MedSearch IR** is a prototype healthcare Information Retrieval (IR) system developed as part of the University of the People's CS 3308 course.

The objective of this project is to design, implement, and evaluate a realistic search engine capable of retrieving relevant medical information using classical Information Retrieval techniques. The project also discusses modern neural retrieval approaches and Retrieval-Augmented Generation (RAG) as future extensions.

---

# Objectives

- Design a complete Information Retrieval pipeline.
- Implement document preprocessing and indexing.
- Compare multiple ranking algorithms.
- Evaluate retrieval effectiveness using standard IR metrics.
- Analyze fairness and optimization strategies.
- Produce a reproducible implementation supporting the final project report.

---

# Repository Structure

```text
MedSearch_IR/
│
├── dataset/                 # Datasets used by the project
│
├── docs/
│   └── diagrams/            # System diagrams and architecture figures
│
├── results/
│   ├── charts/              # Generated plots
│   └── evaluation_results.csv
│
├── src/
│   ├── crawler/
│   ├── preprocessing/
│   ├── indexing/
│   ├── ranking/
│   └── evaluation/
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Features

## Data Collection

- [ ] Document collection
- [ ] Web crawler
- [ ] Dataset preparation

## Text Processing

- [ ] HTML cleaning
- [ ] Text normalization
- [ ] Tokenization
- [ ] Stopword removal
- [ ] Stemming / Lemmatization

## Indexing

- [ ] Inverted Index
- [ ] TF-IDF representation
- [ ] BM25 indexing

## Retrieval & Ranking

- [ ] Keyword search
- [ ] TF-IDF ranking
- [ ] BM25 ranking
- [ ] Learning-to-Rank (LTR)

## Evaluation

- [ ] Precision
- [ ] Recall
- [ ] F1 Score
- [ ] MAP
- [ ] nDCG
- [ ] A/B Testing
- [ ] Performance visualization

## Future Enhancements

- [ ] Semantic search
- [ ] Sentence embeddings
- [ ] BERT / ColBERT retrieval
- [ ] Conversational search
- [ ] Retrieval-Augmented Generation (RAG)

---

# Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3 |
| Crawling | Requests, BeautifulSoup |
| Data Processing | Pandas, NumPy |
| NLP | NLTK |
| Ranking | TF-IDF, BM25 |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib |
| Version Control | Git & GitHub |

---

# Development Workflow

This repository is dedicated to **source code** and reproducible experiments.

Project management, report writing, and presentation materials are maintained separately.

| Resource | Purpose |
|----------|---------|
| GitHub | Source code and version control |
| Google Drive | Report, presentation, and shared documents |
| Todoist | Task management and project tracking |

---

# Getting Started

Clone the repository:

```bash
git clone https://github.com/amm926616/MedSearch_IR.git
cd MedSearch_IR
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

# Project Status

Current implementation progress:

- [x] Repository initialized
- [x] Project structure created
- [ ] Data collection
- [ ] Preprocessing
- [ ] Indexing
- [ ] Ranking
- [ ] Evaluation
- [ ] Report integration

---

# Contributors

| Member | Responsibilities |
|---------|------------------|
| Member 1 | Project coordination, architecture, indexing, evaluation, report integration |
| Member 2 | Crawling, preprocessing, ranking, documentation, presentation |

---

# License

This project was developed for academic purposes as part of the **CS 3308 – Information Retrieval** course at the **University of the People**.
