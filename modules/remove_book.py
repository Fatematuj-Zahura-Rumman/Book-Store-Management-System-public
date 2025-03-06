def remove_book(books):
    remove = input("Enter ISBN of the book to remove: ")
    
    # Find and remove the book
    for i, book in enumerate(books):
        if book['ISBN'] == remove:
            del books[i]
            print(f"Book with ISBN {remove} has been removed.")
            return

    print(f"No book found with ISBN {remove}.")
