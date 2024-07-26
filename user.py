class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        self.__borrowed_books.remove(book)

    def get_borrowed_books(self):
        return self.__borrowed_books

    def __str__(self):
        return f"{self.__name} (Library ID: {self.__library_id})"
