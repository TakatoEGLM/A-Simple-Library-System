from OOPPythonLab5 import *

class LibraryApp:
    def __init__(self):
        self.library = Library()
        self.current_user = None

    def login(self):
        username = input("Enter your username: ")
        user_type = input("Are you an Admin, Operator, or Regular user? (admin/operator/regular): ").strip().lower()
        if user_type == "admin":
            self.current_user = AdminUser(username)
        elif user_type == "operator":
            self.current_user = OperatorUser(username)
        elif user_type == "regular":
            self.current_user = RegularUser(username)
        else:
            print("Invalid user type. Please try again.")
            self.login()

    def logout(self):
        print("\nLogging out...")
        self.current_user = None
        self.login()

    def main_menu(self):
        self.login()
        while True:
            print("\n=== Main Menu ===")
            print("1. View the library catalog.")
            print("2. Search for a book in the library.")
            if isinstance(self.current_user, (AdminUser, OperatorUser)):
                print("3. Add a book to the library.")
                print("4. Edit a book from the library.")
                print("5. Remove a book from the library.")
                print("6. Mark all books as unavailable.")
            if isinstance(self.current_user, OperatorUser):
                print("7. Clear all books in the library catalog.")
            print("8. Log out")
            print("0. Exit Library")

            choice = input("Choose an option (1-7/0): ").strip()

            if choice == "1":
                self.current_user.view_library(self.library)
            elif choice == "2":
                keyword = input("Enter a keyword to search: ").strip()
                self.library.search_books(keyword)
            elif choice == "3" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                self.current_user.add_book(self.library)
            elif choice == "4" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                isbn = input("Enter the ISBN of the book to edit: ").strip()
                self.library.edit_book(isbn)
            elif choice == "5" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                isbn = input("Enter the ISBN of the book to remove: ").strip()
                self.library.remove_book(isbn)
            elif choice == "6" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                self.library.mark_all_unavailable()
            elif choice == "7" and isinstance(self.current_user, OperatorUser):
                self.library.remove_all_books(self.library)
            elif choice == "8":
                self.logout()
            elif choice == "0":
                print("Exiting the program. Goodbye!")
                print("=============================")
                break
            else:
                print("Invalid option. Please choose a valid option.")
                
if __name__ == "__main__":
    print("=== Welcome to Library ===\n")
    app = LibraryApp()
    app.main_menu()
