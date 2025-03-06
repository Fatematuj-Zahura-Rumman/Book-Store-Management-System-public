BOOKS_FILE = 'data.txt'

def load_books():
    books = []
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            next(file)# Skip the header line
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 6:
                    books.append({
                        'title': parts[0],
                        'author': parts[1],
                        'ISBN': parts[2],
                        'genre': parts[3],
                        'price': float(parts[4]),
                        'stock': int(parts[5])
                    })
    except FileNotFoundError:
        pass
    return books

def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
        
        file.write("Title|Author|ISBN|Genre|Price|Stock\n")
        
        for i in books:
            # Write each book in the same format
            file.write(f"{i['title']}|{i['author']}|{i['ISBN']}|{i['genre']}|{i['price']}|{i['stock']}\n")
