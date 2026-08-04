# A/B Testing

## Overview

A/B testing compares two different ranking approaches to determine which provides better search results.

The MedSearch IR project compares:

- TF-IDF ranking
- BM25 ranking

Both systems receive identical queries and are evaluated using the same relevance judgments.

---

# Experiment Design

The experiment follows this structure:

````

```
          Query

            |

    +---------------+

    |               |

  TF-IDF          BM25

    |               |

Ranked Docs    Ranked Docs

    |               |

    +---------------+

            |

       Evaluation

            |

         MAP Score
```

````

---

# System A: TF-IDF

TF-IDF ranks documents based on:

- Term frequency (TF)
- Inverse document frequency (IDF)

Important terms appearing frequently in a document but rarely across the collection receive higher importance.

---

# System B: BM25

BM25 improves traditional TF-IDF by considering:

- document length
- term saturation
- query term frequency

It is widely used in modern search engines.

---

# Experiment Results

The experiment produced:

```

results/ab_test_results.csv

```

Example:

| Query | TF-IDF MAP | BM25 MAP | Winner |
|-|-|-|-|
| blood pressure | 1.0 | 1.0 | Tie |
| diabetes | 1.0 | 1.0 | Tie |

---

# Analysis

Both ranking approaches produced identical results on the current dataset.

This occurred because:

- the corpus contains only five documents
- queries are highly related to document topics
- relevant documents are easy to identify

In larger collections, BM25 would typically provide stronger ranking because it handles document length normalization and term frequency more effectively.

---

# Future Improvements

Future A/B testing could include:

- larger medical datasets
- user click feedback
- statistical significance testing
- online experiments
- ranking algorithms based on machine learning

---

# Summary

The A/B testing component provides an experimental framework for comparing ranking algorithms and supports future optimization of the MedSearch IR ranking system.
