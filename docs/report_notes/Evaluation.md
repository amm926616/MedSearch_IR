# Evaluation

## Overview

Evaluation measures how effectively the MedSearch IR system retrieves relevant medical documents.

The project evaluates retrieval performance using standard Information Retrieval metrics:

- Precision
- Recall
- F1-score
- Mean Average Precision (MAP)
- Normalized Discounted Cumulative Gain (nDCG)

These metrics measure both retrieval accuracy and ranking quality.

---

# Relevance Judgments

The evaluation process uses query relevance judgments stored in:

````

dataset/qrels/qrels.json

````

The qrels file defines which documents are considered relevant for each query.

Example:

```json
{
    "blood pressure": {
        "DOC0002": 2,
        "DOC0003": 1
    }
}
````

The relevance score indicates the importance of each document.

---

# Precision

Precision measures how many retrieved documents are relevant.

Formula:

```
Precision =
Relevant Retrieved Documents
/
Total Retrieved Documents
```

High precision means the search engine returns fewer irrelevant results.

---

# Recall

Recall measures how many relevant documents were successfully retrieved.

Formula:

```
Recall =
Relevant Retrieved Documents
/
Total Relevant Documents
```

High recall means the system finds most relevant information.

---

# F1 Score

F1 combines precision and recall.

Formula:

```
F1 =
2 × Precision × Recall
/
Precision + Recall
```

It provides a balance between retrieving enough documents and avoiding irrelevant results.

---

# Mean Average Precision (MAP)

MAP evaluates ranking quality across multiple queries.

It considers:

- position of relevant documents
    
- ordering of retrieved results
    
- consistency across queries
    

Higher MAP indicates better ranking performance.

---

# nDCG

Normalized Discounted Cumulative Gain evaluates ranked search results while considering document position.

Documents appearing higher in the ranking contribute more value.

This is important because users usually focus on the first few search results.

---

# Evaluation Results

The current evaluation dataset produced:

|Query|Precision|Recall|F1|MAP|nDCG|
|---|---|---|---|---|---|
|blood pressure|1.0|1.0|1.0|1.0|1.0|
|diabetes|1.0|1.0|1.0|1.0|1.0|
|influenza|1.0|1.0|1.0|1.0|1.0|

---

# Limitations

Although the system achieved perfect scores, the evaluation dataset is small.

The results demonstrate correct implementation but do not represent real-world performance.

Future evaluation should include:

- larger medical collections
    
- more diverse queries
    
- expert-created relevance judgments
    
- user-based testing
    

---

# Summary

The evaluation component verifies that the MedSearch IR system can successfully retrieve and rank relevant medical documents using standard IR evaluation methodology.