# Initial proposal
class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter:
    def format(self, book: Book):
        return book.content


class DesktopFormatter(BaseFormatter):
    def format(self, book):
        return book.content[:20]


class OnlineFormatter(BaseFormatter):
    def format(self, book):
        return book.content[:100]


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: BaseFormatter):
        return formatter.format(book)


printer = Printer()
formatter = OnlineFormatter()
print(printer.get_book(Book("Hello I am kajbdhks;b;dbf;KDBF;WW/FB"), formatter))
formatter = DesktopFormatter()
print(printer.get_book(Book("Hello I am kajbdhks;b;dbf;KDBF;WW/FB"), formatter))
