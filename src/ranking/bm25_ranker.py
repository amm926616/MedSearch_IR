"""
bm25_ranker.py

BM25 ranking implementation.
"""


import math



class BM25Ranker:


    def __init__(
        self,
        index,
        metadata,
        total_documents
    ):

        self.index = index
        self.metadata = metadata
        self.total_documents = total_documents


        self.k1 = 1.5
        self.b = 0.75


        self.avg_doc_length = (
            sum(
                doc["length"]
                for doc in metadata.values()
            )
            /
            total_documents
        )



    def idf(self, term):

        if term not in self.index:

            return 0


        df = len(
            self.index[term]
        )


        return math.log(
            (
                self.total_documents - df + 0.5
            )
            /
            (
                df + 0.5
            )
            + 1
        )



    def rank(self, query_tokens):

        scores = {}


        for term in query_tokens:


            if term not in self.index:
                continue


            idf = self.idf(term)


            for doc_id, frequency in self.index[term].items():

                doc_length = (
                    self.metadata[doc_id]["length"]
                )


                numerator = (
                    frequency *
                    (self.k1 + 1)
                )


                denominator = (
                    frequency
                    +
                    self.k1 *
                    (
                        1 -
                        self.b
                        +
                        self.b *
                        (
                            doc_length /
                            self.avg_doc_length
                        )
                    )
                )


                score = (
                    idf *
                    (
                        numerator /
                        denominator
                    )
                )


                scores[doc_id] = (
                    scores.get(doc_id, 0)
                    +
                    score
                )


        return sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )