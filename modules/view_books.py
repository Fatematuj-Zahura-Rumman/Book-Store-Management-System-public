def view_books(books):
    if not books:
        print("No books found.")
        return
    
    print("\nList of Books: ")
    print("-------------------------")
    for i in books:
        print(f" Title: {i['title']},\n Author:{i['author']},\n ISBN: {i['ISBN']},\n Genre: {i['genre']},\n Price: {i['price']},\n Stock:{i['stock']}")
        print("-------------------------")
