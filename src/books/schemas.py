from pydantic import BaseModel

from authors.schemas import Author


class Book(BaseModel):
    book_id: int
    title: str
    author: Author
