from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author
from genre import Genre

books = []
users = []
authors = []
genres = []

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Select an option: ")
        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to main menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def genre_operations():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to main menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")
    publication_date = input("Enter the publication date: ")
    genre_name = input("Enter the genre: ")
    genre = next((g for g in genres if g.get_name() == genre_name), None)
    if genre:
        book = Book(title, author, isbn, publication_date, genre)
        books.append(book)
        print(f"Book '{title}' added successfully.")
    else:
        print(f"Genre '{genre_name}' not found. Please add the genre first.")

def borrow_book():
    isbn = input("Enter the ISBN of the book to borrow: ")
    book = next((b for b in books if b.get_isbn() == isbn), None)
    if book and book.is_available():
        user_id = input("Enter the library ID of the user: ")
        user = next((u for u in users if u.get_library_id() == user_id), None)
        if user:
            book.set_available(False)
            user.borrow_book(book)
            print(f"Book '{book.get_title()}' borrowed by {user.get_name()}.")
        else:
            print(f"User with library ID '{user_id}' not found.")
    else:
        print(f"Book with ISBN '{isbn}' not found or not available.")

def return_book():
    isbn = input("Enter the ISBN of the book to return: ")
    book = next((b for b in books if b.get_isbn() == isbn), None)
    if book and not book.is_available():
        user_id = input("Enter the library ID of the user: ")
        user = next((u for u in users if u.get_library_id() == user_id), None)
        if user and book in user.get_borrowed_books():
            book.set_available(True)
            user.return_book(book)
            print(f"Book '{book.get_title()}' returned by {user.get_name()}.")
        else:
            print(f"User with library ID '{user_id}' not found or book not borrowed by this user.")
    else:
        print(f"Book with ISBN '{isbn}' not found or already available.")

def search_book():
    isbn = input("Enter the ISBN of the book to search: ")
    book = next((b for b in books if b.get_isbn() == isbn), None)
    if book:
        print(f"Book found: {book}")
    else:
        print(f"Book with ISBN '{isbn}' not found.")

def display_books():
    if books:
        print("\nList of all books:")
        for book in books:
            print(book)
    else:
        print("No books available.")

def add_user():
    name = input("Enter the user's name: ")
    library_id = input("Enter the library ID: ")
    user = User(name, library_id)
    users.append(user)
    print(f"User '{name}' added successfully.")

def view_user_details():
    library_id = input("Enter the library ID of the user: ")
    user = next((u for u in users if u.get_library_id() == library_id), None)
    if user:
        print(f"User details: {user}")
        borrowed_books = user.get_borrowed_books()
        if borrowed_books:
            print("Borrowed books:")
            for book in borrowed_books:
                print(book)
        else:
            print("No books borrowed.")
    else:
        print(f"User with library ID '{library_id}' not found.")

def display_users():
    if users:
        print("\nList of all users:")
        for user in users:
            print(user)
    else:
        print("No users available.")

def add_author():
    name = input("Enter the author's name: ")
    biography = input("Enter the biography: ")
    author = Author(name, biography)
    authors.append(author)
    print(f"Author '{name}' added successfully.")

def view_author_details():
    name = input("Enter the author's name: ")
    author = next((a for a in authors if a.get_name() == name), None)
    if author:
        print(f"Author details: {author}")
    else:
        print(f"Author '{name}' not found.")

def display_authors():
    if authors:
        print("\nList of all authors:")
        for author in authors:
            print(author)
    else:
        print("No authors available.")

def add_genre():
    name = input("Enter the genre name: ")
    description = input("Enter the description: ")
    category = input("Enter the category: ")
    genre = Genre(name, description, category)
    genres.append(genre)
    print(f"Genre '{name}' added successfully.")

def view_genre_details():
    name = input("Enter the genre name: ")
    genre = next((g for g in genres if g.get_name() == name), None)
    if genre:
        print(f"Genre details: {genre}")
    else:
        print(f"Genre '{name}' not found.")

def display_genres():
    if genres:
        print("\nList of all genres:")
        for genre in genres:
            print(genre)
    else:
        print("No genres available.")

if __name__ == "__main__":
    main_menu()
