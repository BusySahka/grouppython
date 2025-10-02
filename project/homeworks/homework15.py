class Book:
    def __init__(self, author, title, book_id):
        self.author = author
        self.title = title
        self.book_id = book_id

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to {self.name}.")

    def remove_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from {self.name}.")
                return
        print(f"No book found with ID {book_id}.")

    def list_books(self):
        if not self.books:
            print(f"{self.name} has no books.")
        else:
            print(f"Books in {self.name}:")
            for book in self.books:
                print(f"- {book}")



