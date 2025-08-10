from .repository import BookRepository
from .schemas import Book


class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def get_books(self) -> list[Book]:
        return self.book_repository.get_all_books()

    def get_book(self, book_id: int) -> Book:
        return self.book_repository.get_book_by_id(book_id)
