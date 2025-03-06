def add_book(books):
    print("\nEnter book details:")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    genre = input("Genre: ")
    price = float(input("Price: "))
    stock = int(input("Quantity in stock: "))

    
    if any(i['ISBN'] == isbn for i in books): # Check if ISBN already exists
        print("Error: A book with this ISBN already exists.")
        return

    books.append({
        'title': title,
        'author': author,
        'ISBN': isbn,
        'genre': genre,
        'price': price,
        'stock': stock
    })
    print(f"Book '{title}' by {author} is added.")
