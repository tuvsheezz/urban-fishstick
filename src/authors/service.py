from .repository import AuthorRepository
from .schemas import Author


class AuthorService:
    def __init__(self, author_repository: AuthorRepository) -> None:
        self.author_repository: AuthorRepository = author_repository

    def get_authors(self) -> list[Author]:
        return self.author_repository.get_all_authors()

    def get_author(self, author_id: int) -> Author:
        return self.author_repository.get_author_by_id(author_id)
