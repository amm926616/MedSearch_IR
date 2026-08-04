"""
postings.py

Stores document IDs and term frequencies.
"""


class PostingList:
    """
    Stores term frequency information.

    Example:

    {
        "DOC0001": 3,
        "DOC0002": 1
    }

    Meaning:

    DOC0001 contains the term 3 times.
    DOC0002 contains the term 1 time.
    """

    def __init__(self):

        self.documents = {}


    def add(self, document_id):

        if document_id not in self.documents:

            self.documents[document_id] = 1

        else:

            self.documents[document_id] += 1



    def get_documents(self):

        return self.documents