from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title one', 'author': 'Author one', 'category': 'science'},
    {'title': 'Title two', 'author': 'Author two', 'category': 'science'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'history'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'math'},
    {'title': 'Title five', 'author': 'Author five', 'category': 'math'},
    {'title': 'Title six', 'author': 'Author two', 'category': 'math'}
]

@app.get('/books')
def read_all_books():
    return BOOKS


@app.get('/books/{book_title}')
async def read__book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return




@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []

    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
            return books_to_return


@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


@app.put('/books/update_book')
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get('/author/')
async def fetch_all_books_by_query(name: str):
    books_to_return = []

    for book in BOOKS:
        if book.get('author').casefold() == name.casefold():
            books_to_return.append(book)
            
    return books_to_return

@app.get('/author/{author_name}')
async def fetch_all_books(author_name: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            books_to_return.append(book)
    return books_to_return