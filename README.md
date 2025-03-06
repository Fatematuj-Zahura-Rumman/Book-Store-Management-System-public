# Book-Store-Management-System-public
Simple Book Store Management System using python

Book as class to store information like title, author, ISBN, genre, price, and stock.

.txt file to store books.

different modules for task. -book_data.py: This will handle loading, saving, and modifying the book data (reading/writing from/to files). -add_book.py: A module for adding books to the system. -view_books.py: A module for displaying books in a user-friendly way. -remove_book.py: A module for removing books by their ISBN or Book ID. -search_books.py: This module will handle searching for books by different attributes like title, author, or ISBN. -main.py: The entry point of the application. It will handle the main menu, user input, and call the relevant modules.

Main Menu & Navigation: When the program starts, load the existing data (if available) Show the menu: (1) Add Book (2) View Books (3) Remove Book (4) Search Book (5) Exit (saves all the data back to the file)

5.Add Book: Take user input for book detailes. make sure the ISBM Id is unique. append the data to the file.

6.View Books: Read and display all saved books

7.Remove Book: Ask for the ISBN to be removed. If found, remove it from the file. If not found, provide an error message.

8.Search Books: Search for books by title. Display matching books.
