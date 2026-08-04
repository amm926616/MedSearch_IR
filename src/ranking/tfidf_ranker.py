"""
tfidf_ranker.py

Ranks documents using TF-IDF scoring.
"""

import math


class TFIDFRanker:


    def __init__(self, index, total_documents):

        self.index = index
        self.total_documents = total_documents



    def calculate_idf(self, term):

        if term not in self.index:

            return 0


        document_frequency = len(
            self.index[term]
        )


        return math.log(
            self.total_documents /
            document_frequency
        )



    def score(
        self,
        query_tokens
    ):

        scores = {}


        for term in query_tokens:


            if term not in self.index:
                continue


            idf = self.calculate_idf(term)


            for document, frequency in self.index[term].items():

                tfidf = frequency * idf


                if document not in scores:

                    scores[document] = 0


                scores[document] += tfidf


        return scores



    def rank(
        self,
        query_tokens
    ):

        scores = self.score(
            query_tokens
        )


        return sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )