from fastapi import APIRouter, Depends

from src.authors.repository import AuthorRepository

from .repository import BookRepository
from .schemas import Book
from .service import BookService

router = APIRouter()


def get_book_service() -> BookService:
    book_repository = BookRepository()
    author_repository = AuthorRepository()
    return BookService(book_repository, author_repository)


@router.get("", response_model=list[Book])
async def read_books(
    book_service: BookService = Depends(get_book_service),
) -> list[Book]:
    return book_service.get_books()


@router.get("/{book_id}", response_model=Book)
async def read_book(
    book_id: int, book_service: BookService = Depends(get_book_service)
) -> Book:
    return book_service.get_book(book_id)
