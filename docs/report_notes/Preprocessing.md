# Text Preprocessing Design

## Overview

Text preprocessing is the second stage of the MedSearch IR pipeline.

The purpose of preprocessing is to transform raw medical documents into a normalized format that can be efficiently indexed and searched.

Raw medical text contains many elements that reduce retrieval accuracy:

- Uppercase/lowercase variations
- Punctuation
- Common words with little search value
- Different forms of the same word
- HTML or formatting noise

The preprocessing module cleans and transforms documents before indexing.

---

# Pipeline Position

The complete system flow:

```
Medical Sources
        |
        ↓
medical_articles.csv
        |
        ↓
dataset_loader.py
        |
        ↓
raw_documents.json
        |
        ↓
Text Preprocessing
        |
        ↓
processed_documents.json
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

# Preprocessing Pipeline

The preprocessing process consists of five stages:

## 1. Text Normalization

Purpose:

Convert different text forms into a consistent representation.

Operations:

- Convert text to lowercase
- Remove unnecessary whitespace
- Normalize special characters


Example:

Before:

```
Tuberculosis IS an Infectious Disease!!!
```

After:

```
tuberculosis is an infectious disease
```

---

# 2. Tokenization

Purpose:

Split text into individual terms.

Example:

Input:

```
high blood pressure is dangerous
```

Output:

```
[
"high",
"blood",
"pressure",
"is",
"dangerous"
]
```

Tokens become the basic units used by the search engine.

---

# 3. Stopword Removal

Purpose:

Remove common words that provide little retrieval value.

Examples:

```
the
is
a
an
of
and
```

Before:

```
diabetes is a disease of metabolism
```

After:

```
diabetes disease metabolism
```

---

# 4. Stemming

Purpose:

Reduce related words to a common root.

Examples:

```
diseases
disease

infectious
infection
```

Possible normalized form:

```
disease
infect
```

This improves matching between user queries and documents.

---

# 5. Lemmatization (Future Enhancement)

Lemmatization converts words into their dictionary form.

Example:

```
running → run

children → child
```

For the first implementation, stemming will be used because it is faster and simpler.

---

# Input and Output

## Input

File:

```
dataset/processed/raw_documents.json
```

Example:

```json
{
    "DOC0001": {
        "text": "Tuberculosis is an infectious disease..."
    }
}
```

---

## Output

File:

```
dataset/processed/processed_documents.json
```

Example:

```json
{
    "DOC0001": {
        "tokens": [
            "tuberculosi",
            "infect",
            "diseas"
        ]
    }
}
```

---

# Module Responsibilities

```
preprocessing/

├── cleaner.py
│   Removes unwanted characters
│
├── tokenizer.py
│   Splits text into tokens
│
├── stopwords.py
│   Removes common words
│
├── stemmer.py
│   Reduces words to roots
│
├── normalizer.py
│   Controls text normalization
│
└── pipeline.py
    Runs the complete preprocessing workflow
```

---

# Design Principles

## Single Responsibility

Each module performs one specific operation.

Example:

`tokenizer.py`

Only tokenizes.

It does not remove stopwords or perform stemming.

---

## Reusability

The preprocessing pipeline should work with:

- WHO documents
- PubMed articles
- CDC pages
- NIH resources

without modification.

---

## Extensibility

Future improvements:

- Medical terminology normalization
- Named entity recognition
- MeSH vocabulary mapping
- Clinical concept extraction