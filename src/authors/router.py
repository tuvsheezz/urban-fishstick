from fastapi import APIRouter, Depends

from .repository import AuthorRepository
from .schemas import Author
from .service import AuthorService

router = APIRouter()


def get_author_service() -> AuthorService:
    repository = AuthorRepository()
    return AuthorService(repository)


@router.get("", response_model=list[Author])
async def read_authors(
    author_service: AuthorService = Depends(get_author_service),
) -> list[Author]:
    return author_service.get_authors()


@router.get("/{author_id}", response_model=Author)
async def read_author(
    author_id: int, author_service: AuthorService = Depends(get_author_service)
) -> Author:
    return author_service.get_author(author_id)
