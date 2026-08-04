# Search Engine Module

## Overview

The Search Engine module provides the user-facing search functionality of the MedSearch IR system.

While previous components focus on collecting, preprocessing, indexing, and ranking documents, the Search Engine module integrates these components into a complete information retrieval workflow.

The module allows users to submit medical queries and receive ranked medical documents based on relevance.

---

# System Position

The Search Engine is located at the final stage of the retrieval pipeline:

```
Medical Sources
      |
      v
Collection Module
      |
      v
Raw Documents
      |
      v
Preprocessing
      |
      v
Processed Documents
      |
      v
Inverted Index
      |
      v
Ranking Algorithm
      |
      v
Search Engine
      |
      v
User Results
```

---

# Purpose

The main responsibilities of the Search Engine module are:

- Loading the generated search index
- Loading document metadata
- Processing user queries
- Applying ranking algorithms
- Returning ranked results
- Displaying useful document information

---

# Implementation

The main implementation is located at:

```
src/query/search_engine.py
```

The module connects three important components:

```
SearchEngine

      |
      |
      +---- QueryProcessor
      |
      +---- Inverted Index
      |
      +---- BM25Ranker
      |
      +---- Document Metadata
```

---

# Data Loading

When the Search Engine starts, it loads three important files.

## 1. Inverted Index

Location:

```
dataset/processed/inverted_index.json
```

Purpose:

The inverted index maps terms to documents containing those terms.

Example:

```json
{
    "blood": {
        "DOC0002": 2,
        "DOC0003": 1
    }
}
```

This allows efficient document retrieval without scanning every document.

---

## 2. Document Metadata

Location:

```
dataset/processed/document_metadata.json
```

Purpose:

Stores document statistics required by BM25 ranking.

Example:

```json
{
    "DOC0002": {
        "length": 20
    }
}
```

The metadata is used to calculate document length normalization.

---

## 3. Processed Documents

Location:

```
dataset/processed/processed_documents.json
```

Purpose:

Stores document information displayed to users.

Example:

```json
{
    "DOC0002": {
        "title": "High Blood Pressure",
        "source": "NIH",
        "url": "..."
    }
}
```

---

# Query Processing

User queries are processed using the same preprocessing pipeline applied to documents.

Example:

User query:

```
blood pressure
```

Before searching:

```
blood pressure
```

is transformed into:

```
[
    "blood",
    "pressur"
]
```

This ensures consistency between document indexing and query retrieval.

---

# Ranking

The Search Engine uses BM25 ranking.

BM25 improves retrieval quality by considering:

- Term frequency
- Document frequency
- Document length
- Query term importance

The ranking process:

```
User Query

      |
      v

Query Processing

      |
      v

Search Terms

      |
      v

BM25 Scoring

      |
      v

Ranked Documents
```

---

# Search Result Format

The system returns:

- Document title
- Source
- URL
- BM25 relevance score

Example:

```
Title  : High Blood Pressure

Source : NIH

Score  : 2.4554

URL    : https://www.nhlbi.nih.gov/health/high-blood-pressure
```

---

# Design Advantages

## Modularity

The Search Engine does not implement indexing or ranking algorithms directly.

Instead, it communicates with independent modules.

This follows the principle of separation of concerns.

---

## Extensibility

Future improvements can be added without redesigning the system:

- TF-IDF ranking
- Learning-to-Rank models
- Semantic embeddings
- Personalized search
- Medical knowledge graphs

---

# Future Improvements

Possible enhancements include:

## Multiple Ranking Models

Allow users to select:

- BM25
- TF-IDF
- Hybrid ranking

---

## Query Expansion

Medical queries could be expanded using:

- Synonyms
- Medical terminology databases
- Ontologies such as UMLS

Example:

```
heart attack

+

myocardial infarction
```

---

## Online Search

The Search Engine can later connect with the crawler module to retrieve newly collected medical documents.

---

# Summary

The Search Engine module transforms MedSearch IR from a collection of independent components into a complete Information Retrieval application.

It connects:

- Query processing
- Index searching
- BM25 ranking
- Document presentation

to provide users with ranked medical information.