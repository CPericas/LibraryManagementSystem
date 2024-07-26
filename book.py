class Book:
    def __init__(self, title, author, isbn, publication_date, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__available = True
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__available

    def set_available(self, status):
        self.__available = status

    def get_genre(self):
        return self.__genre

    def __str__(self):
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn})"

class FictionBook(Book):
    pass

class NonFictionBook(Book):
    pass

