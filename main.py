from modules.add_book import add_book
from modules.view_books import view_books
from modules.remove_book import remove_book
from modules.search_books import search_books
from modules.book_data import load_books, save_books


#Shows the main menu after running the code
def main_menu():
    print("------------------------------------------")
    print("       Welcome to the Book Store!")
    print("------------------------------------------")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

def main():
# Load books from the file on start
    books = load_books()

    while True:
        main_menu()
        choice = input("Please enter your choice: ")

        if choice == '1':
            add_book(books) 
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            search_books(books) 
        elif choice =='4':
            remove_book(books)
        elif choice == '5':
            save_books(books)  
            print("Thank you for using this system. See you next time.")
            print("-----------------------------------------------------")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()