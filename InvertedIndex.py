# Original version: https://medium.com/@fro_g/writing-a-simple-inverted-index-in-python-3c8bcb52169a
# Some comments were added and structure modified slightly; several functions were removed
# Still there are methods, that require review, since, for example, "remove" method in Database does not modify
# the appearance, where docId with frequency still is presented for deleted document


import re


class Appearance:
    """
    For each word, this class gives ID of the document and frequency of this word in it
    """

    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency


class Database:
    """
    This structure contains documents: id + text
    """

    def __init__(self):
        self.db = dict()

    def get(self, id):
        """
        Get id of the document
        """
        return self.db.get(id, None)

    def add(self, document):
        """
        Adds a document to the DB.
        """
        return self.db.update({document['id']: document})

    def remove(self, document):
        """
        Removes document from DB.
        """
        return self.db.pop(document['id'], None)


class InvertedIndex:
    """
    Inverted Index class.
    """

    def __init__(self, db):
        # dictionary {"word": Appearance}
        self.index = dict()
        # Database with all the documents
        self.db = db

    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """

        # Remove punctuation from the text.
        clean_text = re.sub(r'[^\w\s]', '', document['text'])

        # Split the text into words
        words = clean_text.split(' ')

        # Creation of the dictionary
        appearances_dict = dict()  # Dictionary with each term and the frequency it appears in the text.

        # For each word in words we update its frequency or add it if it is not there
        for word in words:
            word_frequency = appearances_dict[word].frequency if word in appearances_dict else 0
            appearances_dict[word] = Appearance(document['id'], word_frequency + 1)

        # Update the inverted index
        update_dict = {key: [appearance]
                       if key not in self.index
                       else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items()}

        self.index.update(update_dict)

        # Add the document into the database
        self.db.add(document)

        return document

    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances.
        """
        return {term: self.index[term] for term in query.split(' ') if term in self.index}


# Function for highlighting the words in the text
def highlight_term(id, term, text):
    # Python colors: https://newbedev.com/colour-codes-python-code-example
    replaced_text = text.replace(term, f"\033[1;32;40m {term} \033[0;0m")
    return f"Document {id}: {replaced_text}"


def main():
    file_names = input("Enter file names: ").split()

    # Initialization of database
    db = Database()
    index = InvertedIndex(db)

    for id, file_name in enumerate(file_names):
        # File
        file = open(file_name, "r")

        # Document to process
        document = {
            'id': str(id + 1),
            'text': file.read()
        }

        index.index_document(document)

    search_term = input("Enter term(s) to search: ")
    result = index.lookup_query(search_term)

    for term in result.keys():
        for appearance in result[term]:
            document = db.get(appearance.docId)
            print(highlight_term(appearance.docId, term, document['text']))
        print("-----------------------------")


if __name__ == '__main__':
    main()
