from fastapi import HTTPException, status

from .schemas import Author

authors_db: dict[int, Author] = {
    1: Author(author_id=1, name="F. Scott Fitzgerald"),
    2: Author(author_id=2, name="Harper Lee"),
    3: Author(author_id=3, name="George Orwell"),
}


class AuthorRepository:
    def get_all_authors(self) -> list[Author]:
        return list(authors_db.values())

    def get_author_by_id(self, author_id: int) -> Author:
        author = authors_db.get(author_id)
        if author is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Author not found"
            )
        return author
