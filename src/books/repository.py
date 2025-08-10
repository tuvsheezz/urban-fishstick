from fastapi import HTTPException, status

from .schemas import Book

books_db: dict[int, Book] = {
    1: Book(book_id=1, title="The Great Gatsby", author="F. Scott Fitzgerald"),
    2: Book(book_id=2, title="To Kill a Mockingbird", author="Harper Lee"),
    3: Book(book_id=3, title="1984", author="George Orwell"),
}


class BookRepository:
    def get_all_books(self) -> list[Book]:
        return list(books_db.values())

    def get_book_by_id(self, book_id: int) -> Book:
        book = books_db.get(book_id)
        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )
        return book
