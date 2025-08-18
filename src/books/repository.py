from fastapi import HTTPException, status
from pydantic import BaseModel


# このリポジトリが管理するデータの内部表現
class BookInDB(BaseModel):
    book_id: int
    title: str
    author_id: int


books_db: dict[int, BookInDB] = {
    1: BookInDB(book_id=1, title="The Great Gatsby", author_id=1),
    2: BookInDB(book_id=2, title="To Kill a Mockingbird", author_id=2),
    3: BookInDB(book_id=3, title="1984", author_id=3),
}


class BookRepository:
    def get_all_books(self) -> list[BookInDB]:
        return list(books_db.values())

    def get_book_by_id(self, book_id: int) -> BookInDB:
        book: BookInDB | None = books_db.get(book_id)
        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )
        return book
