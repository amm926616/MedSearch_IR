# Ranking in Information Retrieval

## Overview

Ranking is the process of ordering retrieved documents according to their relevance to a user's query.

A basic retrieval system can only determine whether a document contains query terms. However, a practical search engine must decide which documents are more relevant and should appear first.

The MedSearch IR system uses ranking algorithms to improve search quality by assigning relevance scores to documents.

Implemented ranking methods:

1. TF-IDF (Term Frequency-Inverse Document Frequency)
2. BM25 (Best Matching 25)

---

# Why Ranking is Needed

Without ranking, the search engine only performs matching.

Example:

Query:

```
blood pressure
```

Retrieved documents:

```
DOC0002
DOC0003
```

Both documents contain the term "blood", but they are not equally relevant.

DOC0002:

```
High blood pressure is a common condition...
```

Contains both query terms.

DOC0003:

```
Diabetes mellitus is a chronic metabolic disorder...
```

Only contains the word "blood".

Therefore, DOC0002 should receive a higher ranking.

Ranking algorithms calculate relevance scores and return the most useful results first.

---

# TF-IDF Ranking

## Definition

TF-IDF measures the importance of a word in a document compared with the entire document collection.

It combines two values:

- Term Frequency (TF)
- Inverse Document Frequency (IDF)

---

## Term Frequency (TF)

Term Frequency measures how often a term appears inside a document.

Formula:

```
TF(t,d) = frequency of term t in document d
```

Example:

Document:

```
Blood pressure affects blood vessels.
```

Term:

```
blood
```

Frequency:

```
2
```

Higher frequency increases the importance of a term.

---

## Inverse Document Frequency (IDF)

IDF measures how rare or unique a term is across all documents.

Formula:

```
IDF(t) = log(N / df)
```

Where:

- N = total number of documents
- df = number of documents containing the term

A common word has lower importance.

A rare medical term has higher importance.

Example:

```
blood
```

appears in many documents.

Lower IDF.

```
tuberculosis
```

appears in fewer documents.

Higher IDF.

---

## TF-IDF Formula

```
TF-IDF(t,d) = TF(t,d) × IDF(t)
```

The final score represents the importance of a term in a document.

---

# BM25 Ranking

## Definition

BM25 is an improved ranking algorithm based on TF-IDF.

It is widely used in modern search engines because it handles document length and term frequency more effectively.

BM25 considers:

- Term frequency
- Document frequency
- Document length normalization

---

## Advantages of BM25

Compared with TF-IDF:

- Prevents very long documents from receiving unfairly high scores
- Controls the effect of repeated terms
- Produces better ranking results for large collections

BM25 is commonly used in systems such as Apache Lucene and Elasticsearch.

---

# MedSearch IR Ranking Pipeline

The ranking process:

```
User Query

      ↓

Query Processing

      ↓

Document Retrieval

      ↓

Candidate Documents

      ↓

TF-IDF / BM25 Ranking

      ↓

Sorted Search Results
```

---

# Example

Query:

```
blood pressure
```

Candidate documents:

```
DOC0002
DOC0003
```

TF-IDF ranking:

```
1. DOC0002
2. DOC0003
```

Reason:

DOC0002 contains both:

```
blood
pressure
```

while DOC0003 only contains:

```
blood
```

---

# Conclusion

Ranking improves Information Retrieval systems by moving from simple keyword matching to relevance-based search.

The MedSearch IR project implements classical ranking approaches to provide more accurate medical document retrieval.