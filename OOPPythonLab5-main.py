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
            print("1. View the library catalog")
            print("2. Search books from the library")

            if isinstance(self.current_user, (AdminUser, OperatorUser)):
                print("3. Add a book to the library")
                print("4. Edit a book from the library")
                print("5. Remove a book from the library")
                print("6. Mark all books from library as unavailable")
            
            if isinstance(self.current_user, (OperatorUser)):
                print("7. Clear the library catalog")

            print("\n8. Log out")
            print("0. Exit Library")

            choice = input("\nChoose an option (1-8/0): ").strip()

            if choice == "1":
                self.current_user.view_library(self.library)
            elif choice == "2":
                self.current_user.search_books(self.library)
            elif choice == "3" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                self.current_user.add_book(self.library)
            elif choice == "4" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                self.current_user.edit_book(self.library)
            elif choice == "5" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                self.current_user.remove_book(self.library)
            elif choice == "6" and isinstance(self.current_user, (AdminUser, OperatorUser)):
                self.current_user.mark_all_unavailable(self.library)
            elif choice == "7" and isinstance(self.current_user, (OperatorUser)):
                self.current_user.remove_all_books(self.library)
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
    book1 = Book("titlee","authorr","0000000000000","genree")
    app = LibraryApp()
    app.main_menu()