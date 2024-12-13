class Book:
    def __init__(self, title, author, isbn, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.status = True

    def __str__(self):
        if self.status == True:
            return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Status: Available"
        else:
            return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Status: Unavailable"

    # Getter methods
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_genre(self):
        return self.__genre

    # Setter methods
    def set_title(self, new_title):
        while True:
            if not new_title.isalpha():
                print("Invalid Title name. It must contain a string.")
                self.set_title()
            else:
                self.__title = new_title
                break

    def set_author(self, new_author):
        while True:
            if not new_author.isalpha() or len(new_author) > 20:
                print("Invalid Author name. It must contain a string or will not exceed 20 characters.")
                self.set_author()
            else:
                self.__author = new_author
                break

    def set_isbn(self, new_isbn):
        while True:
            if not new_isbn.isdigit() or len(new_isbn) != 13:
                print("Invalid ISBN. It must be a 13-digit number.")
                self.set_isbn()
            else:
                self.__isbn = new_isbn
                break

    def set_genre(self, new_genre):
        self.__genre = new_genre

    def toggle_status(self):
        self.status = not self.status


class Library:
    def __init__(self):
        self.__library = []

    def view_library(self):
        if not self.__library:
            print("\nThe library is empty.")
        else:
            print("\nLibrary Catalog:")
            for index, book in enumerate(self.__library, start=1):
                print(f"\nBook {index}: {book}")

    def add_book(self):
        new_book = Book("", "", "", "")
        while True:
            isbn = input("Enter the ISBN of the book: ")
            new_book.set_isbn(isbn)
            if new_book.get_isbn() == isbn:
                break
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        new_book.set_title(title)
        new_book.set_author(author)
        new_book.set_genre(genre)

        self.__library.append(new_book)
        print("\nNew Book Added: ")
        print(new_book)

    def edit_book(self, isbn):
        if not self.__library:
            print("\nThe library is empty.")
            return
        
        for book in self.__library:
            if book.get_isbn() == isbn:
                print("\nEditing Book:")
                print(book)
                
                while True:
                    print("\nWhat would you like to edit?")
                    print("1. Title")
                    print("2. Author")
                    print("3. Genre")
                    print("4. Toggle Status")
                    print("0. Exit Edit Menu")
                    choice = input("Enter your choice (1/2/3/4/0): ")
                    
                    if choice == "1":
                        new_title = input("Enter the new title: ").strip()
                        book.set_title(new_title)
                        print("Title updated successfully.")
                    elif choice == "2":
                        new_author = input("Enter the new author: ").strip()
                        book.set_author(new_author)
                        print("Author updated successfully.")
                    elif choice == "3":
                        new_genre = input("Enter the new genre: ").strip()
                        book.set_genre(new_genre)
                        print("Genre updated successfully.")
                    elif choice == "4":
                        book.toggle_status()
                        print(f"Book status toggled. New status: {'Available' if book.status else 'Unavailable'}.")
                    elif choice == "0":
                        print("Exiting edit menu.")
                        return
                    else:
                        print("Invalid choice. Please try again.")
                return
        
        print("The book doesn't exist.")

    def remove_book(self, isbn):
        if not self.library:
            print("\nThe library is already empty.")
        else:
            for book in self.library:
                if book.get_isbn() == isbn:
                    self.library.remove(book)
                    print("The book has been deleted successfully.")
                    return
            print("The book doesn't exist.")

    def remove_all_books(self):
        self.__library.clear()
        print("All books have been removed from the library.")

    def get_books(self):
        return self.__library

    def search_books(self, keyword):
        books = self.get_books()
        results = [book for book in books if
                   keyword.lower() in book.get_title().lower() or keyword.lower() in book.get_author().lower()]
        if results:
            print("\nSearch Results:")
            for book in results:
                print(book)
        else:
            print("\nNo books match the search keyword.")

    def mark_all_unavailable(self):
        books = self.get_books()
        for book in books:
            if book.status:
                book.toggle_status()
        print("\nAll books have been marked as unavailable.")


class User:
    def __init__(self, username):
        self.username = username

    def view_library(self, library):
        library.view_library()

    def search_books(self, library):
        keyword = input("Enter the keyword of a book: ")
        library.search_books(keyword)


class OperatorUser(User):
    def view_library(self, library):
        super().view_library(library)
        print(
            "You are browsing as Operator User. You can search and preview books, add, delete books, and clear library catalog.")

    def search_books(self, library):
        super().search_books(library)

    def add_book(self, library):
        library.add_book()

    def remove_book(self, library):
        isbn = input("Enter the isbn of the book to be deleted: ")
        library.remove_book(isbn)

    def remove_all_books(self, library):
        library.remove_all_books()

    def edit_book(self, library):
        isbn = input("Enter the ISBN of the book to be edited: ")
        library.edit_book(isbn)

    def mark_all_unavailable(self, library):
        library.mark_all_unavailable()


class AdminUser(User):
    def view_library(self, library):
        super().view_library(library)
        print("You are browsing as Admin User. You can search and preview books, add, and delete books.")

    def search_books(self, library):
        super().search_books(library)

    def add_book(self, library):
        library.add_book()

    def remove_book(self, library):
        isbn = input("Enter the isbn of the book to be deleted: ")
        library.remove_book(isbn)

    def edit_book(self, library):
        isbn = input("Enter the ISBN of the book to be edited: ")
        library.edit_book(isbn)

    def mark_all_unavailable(self, library):
        library.mark_all_unavailable()


class RegularUser(User):
    def search_books(self, library):
        super().search_books(library)

    def view_library(self, library):
        super().view_library(library)
        print("You are browsing as Regular User. You can only search and preview books.")
