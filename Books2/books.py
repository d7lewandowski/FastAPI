from fastapi import FastAPI, Body, Path, Query, HTTPException

from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str
    published_date: int 

    def __init__(self, id, title, author, description, rating, published_date):

        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
    
class BookRequest(BaseModel):
    id: int = Field(description='ID is not needed to create', default = None) 
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(min_length=4)

    model_config = {
        "json_schema_extra" : {
            "example": {
                "title": " A new book",
                "author": 'codywithdam',
                'description': "A new description of a book",
                "raiting": 5,
                'published_date': 2019
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithdam', 'A very nice book', 5, 2004),
    Book(2, 'Be fast as API', 'codingwithdam', 'Great book', 5, 2004),
    Book(3, 'Science Pro', 'codingwithdam', 'A very nice book', 5, 2010),
    Book(4, 'XXXScience Pro', 'Author 1', 'book desc', 3, 2022),
    Book(5, 'HP1 Science Pro', 'Author 2', 'book desc', 2, 1966),
    Book(6, 'HP3 Pro', 'Author 3', 'book desc', 1, 2022)
]

@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')
        
@app.get('/books/')
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.post('/create-book')
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))



def find_book_id(book: Book):

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    
    return book

@app.put('/books/update_book')
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    
    if not book_changed:
        raise HTTPException(statu_code=404, detail = 'Item not found')

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
        if not book_changed:
            raise HTTPException(status_code=404, detail='Item not found')

@app.get('/published_date/')
async def published_date(date: int = Query(gt=1999, lt=2050)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == date:
            books_to_return.append(book)
    
    return books_to_return