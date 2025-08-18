from authors.repository import AuthorRepository
from authors.schemas import Author
from books.repository import BookInDB

from .repository import BookRepository
from .schemas import Book


class BookService:
    def __init__(
        self, book_repository: BookRepository, author_repository: AuthorRepository
    ) -> None:
        self.book_repository: BookRepository = book_repository
        self.author_repository: AuthorRepository = author_repository

    def get_books(self) -> list[Book]:
        books_in_db: list[BookInDB] = self.book_repository.get_all_books()
        return [
            Book(
                book_id=book.book_id,
                title=book.title,
                author=self.author_repository.get_author_by_id(book.author_id),
            )
            for book in books_in_db
        ]

    def get_book(self, book_id: int) -> Book:
        book_in_db: BookInDB = self.book_repository.get_book_by_id(book_id)
        author: Author = self.author_repository.get_author_by_id(book_in_db.author_id)
        return Book(book_id=book_in_db.book_id, title=book_in_db.title, author=author)
