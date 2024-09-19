"""
Program :
Author : Varshilkumar
"""
class Book:
    def _init_(self, title, author, publication_year, availability_status):
     
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability_status = availability_status

    def display_book_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Availability Status: {'Available' if self.availability_status else 'Not Available'}")

class Patron:

    def _init_(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability_status:
            self.borrowed_books.append(book)
            book.availability_status = False
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability_status = True
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")


class Library:
    def _init_(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"{patron.name} has been registered as a patron.")

    def display_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                print(f"- {book.title} by {book.author} ({book.publication_year})")
        else:
            print("The library has no books.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_patron_by_id(self, patron_id):

        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

library = Library()
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, True)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813, True)
patron1 = Patron("Alice Smith", 1234)
patron2 = Patron("Bob Johnson", 5678)
library.add_book(book1)
library.add_book(book2)
library.register_patron(patron1)
library.register_patron(patron2)
patron1.borrow_book(book1)
patron2.borrow_book(book2)
patron1.display_borrowed_books()
patron2.display_borrowed_books()
library.display_books()
patron1.return_book(book1)
patron1.display_borrowed_books()
library.display_books()
    