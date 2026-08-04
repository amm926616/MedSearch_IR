# Document Collection

## Overview

The document collection component is responsible for acquiring and preparing medical documents before they enter the Information Retrieval pipeline.

In the MedSearch IR project, the collection stage converts different medical information sources into a standardized document format that can be processed by later components.

The system follows an Extract–Transform–Load (ETL) approach.

Medical Sources  
|  
↓  
Document Extraction  
|  
↓  
Standardized Dataset  
|  
↓  
Processing Pipeline

---

## Data Sources

The project uses medical information sources including:

- World Health Organization (WHO)
- National Institutes of Health (NIH)
- PubMed
- Centers for Disease Control and Prevention (CDC)

These sources provide reliable medical information covering diseases, symptoms, treatments, and health conditions.

---

## Dataset Format

Collected documents are stored in:

dataset/raw/medical_articles.csv


The CSV file uses a standardized structure:

| Field | Description |
|---|---|
| id | Unique document identifier |
| source | Origin of the document |
| title | Document title |
| url | Original source URL |
| text | Main document content |

Example:

```csv
DOC0001,WHO,Tuberculosis,https://who.int/...,
Tuberculosis is an infectious disease...
```
```
---

## Dataset Loader

The module:

src/collection/dataset_loader.py

converts the CSV dataset into JSON format.

Input:

medical_articles.csv
```

Output:

```
raw_documents.json
```

Example:

```json
{
    "DOC0001": {
        "source": "WHO",
        "title": "Tuberculosis",
        "text": "Tuberculosis is an infectious disease..."
    }
}
```

---

## Design Purpose

The collection module separates document acquisition from the search engine.

This allows future expansion with additional sources without changing indexing, ranking, or evaluation components.

Possible future sources include:

- Europe PMC
- MedlinePlus
- CDC datasets
- Clinical guideline repositories

---

## Summary

The collection component creates the foundation of the search engine by transforming heterogeneous medical resources into a unified document representation.