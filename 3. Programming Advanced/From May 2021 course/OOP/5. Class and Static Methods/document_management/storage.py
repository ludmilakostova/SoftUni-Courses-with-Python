from document_management.category import Category
from document_management.document import Document
from document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category: Category = [c for c in self.categories if category_id == c.id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic: Topic = list(filter(lambda t: t.id == topic_id, self.topics))[0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document: Document = [doc for doc in self.documents if doc.id == document_id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        cat: Category = [cat for cat in self.categories if cat.id == category_id][0]
        self.categories.remove(cat)

    def delete_topic(self, topic_id):
        top: Topic = [t for t in self.topics if topic_id == t.id][0]
        self.topics.remove(top)

    def delete_document(self, document_id):
        doc: Document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(doc)

    def get_document(self, document_id):
        doc: Document = [d for d in self.documents if d.id == document_id][0]
        return doc

    def __repr__(self):
        result = ""
        docs = "\n".join([d.__repr__() for d in self.documents])
        result += docs
        return docs





