#function for searching a book and printing it
def search_books(books):
    search = input("Enter the title to search book: ").lower() #take the title as input and make it lowercase

    results = [i for i in books if search in i['title'].lower()]

    if not results:
        print("No books found.")
        return
    
    print("-------------------------")
    print("Search Results:")
    
    for i in results:
        print(f" Title: {i['title']},\n Author:{i['author']},\n ISBN: {i['ISBN']},\n Genre: {i['genre']},\n Price: {i['price']},\n Stock:{i['stock']}")
        print("-------------------------")