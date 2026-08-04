"""
inverted_index.py

Manages the weighted inverted index.
"""


from .postings import PostingList



class InvertedIndex:


    def __init__(self):

        self.index = {}



    def add_term(
        self,
        term,
        document_id
    ):


        if term not in self.index:

            self.index[term] = PostingList()


        self.index[term].add(
            document_id
        )



    def search(self, term):

        if term in self.index:

            return self.index[term].get_documents()

        return {}



    def to_dict(self):

        return {

            term: posting.get_documents()

            for term, posting
            in self.index.items()

        }